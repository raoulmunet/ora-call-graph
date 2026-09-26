from __future__ import annotations
from dataclasses import dataclass,asdict
from pathlib import Path
import re

@dataclass(frozen=True)
class Edge:
    caller:str
    callee:str
    file:str
    def to_dict(self): return asdict(self)

def _package_name(sql:str)->str|None:
    m=re.search(r"\bCREATE\s+(?:OR\s+REPLACE\s+)?PACKAGE\s+BODY\s+([A-Za-z][\w$#]*)",sql,re.I)
    return m.group(1).upper() if m else None

def scan_source(sql:str,file:str="<memory>")->list[Edge]:
    pkg=_package_name(sql)
    routines=list(re.finditer(r"\b(?:PROCEDURE|FUNCTION)\s+([A-Za-z][\w$#]*)\b",sql,re.I))
    local_names={m.group(1).upper() for m in routines}
    edges=[]
    for i,m in enumerate(routines):
        name=m.group(1).upper()
        caller=f"{pkg}.{name}" if pkg else name
        body=sql[m.end(): routines[i+1].start() if i+1<len(routines) else len(sql)]
        seen=set()
        for cm in re.finditer(r"\b([A-Za-z][\w$#]*)\.([A-Za-z][\w$#]*)\s*\(",body):
            callee=f"{cm.group(1).upper()}.{cm.group(2).upper()}"
            if callee not in seen and callee!=caller:
                edges.append(Edge(caller,callee,file)); seen.add(callee)
        for local in local_names:
            if local==name: continue
            if re.search(rf"\b{re.escape(local)}\s*\(",body,re.I):
                callee=f"{pkg}.{local}" if pkg else local
                if callee not in seen:
                    edges.append(Edge(caller,callee,file)); seen.add(callee)
    return edges

def scan_path(path:str|Path)->list[Edge]:
    p=Path(path)
    files=[p] if p.is_file() else sorted(p.rglob("*.sql"))
    out=[]
    for f in files:
        out.extend(scan_source(f.read_text(encoding="utf-8"),str(f)))
    return out
