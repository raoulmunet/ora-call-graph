from __future__ import annotations
import argparse,json,re
from .core import scan_path

def main(argv=None):
    p=argparse.ArgumentParser(description="Build a PL/SQL call graph.")
    p.add_argument("source")
    p.add_argument("--format",choices=("text","json","mermaid"),default="text")
    a=p.parse_args(argv)
    edges=scan_path(a.source)
    if a.format=="json":
        print(json.dumps([e.to_dict() for e in edges],indent=2))
    elif a.format=="mermaid":
        print("flowchart LR")
        ids={}
        def node(x):
            if x not in ids: ids[x]=f"N{len(ids)}"
            return ids[x]
        for e in edges:
            print(f'    {node(e.caller)}["{e.caller}"] --> {node(e.callee)}["{e.callee}"]')
    else:
        for e in edges: print(f"{e.caller} -> {e.callee}")
    return 0
if __name__=="__main__": raise SystemExit(main())
