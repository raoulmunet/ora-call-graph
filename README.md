# ora-call-graph

[![tests](https://github.com/raoulmunet/ora-call-graph/actions/workflows/tests.yml/badge.svg)](https://github.com/raoulmunet/ora-call-graph/actions/workflows/tests.yml) ![Python](https://img.shields.io/badge/Python-3.10--3.13-blue) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Build a lightweight call graph from Oracle PL/SQL source.

> **Oracle compatibility**
>
> | Oracle version | Support |
> |---|---|
> | Oracle Database 19c | ✅ Common PL/SQL procedure/function/package syntax |
> | Oracle Database 23ai | ✅ Common PL/SQL procedure/function/package syntax |
> | Oracle AI Database 26ai | ✅ Common PL/SQL procedure/function/package syntax |
>
> Dynamic SQL, polymorphic dispatch and calls resolved through runtime metadata cannot be determined reliably by offline regex/static scanning.

## Features

- scans one `.sql` file or a directory;
- discovers package/procedure/function declarations;
- detects qualified calls such as `PKG_LOG.WRITE_LOG(...)`;
- detects calls to locally declared routines;
- emits text, JSON or Mermaid.

## Usage

```bash
python -m pip install "git+https://github.com/raoulmunet/ora-call-graph.git"

ora-call-graph examples/
ora-call-graph examples/ --format mermaid > calls.mmd
```

Example:

```text
PKG_BATCH.RUN_BATCH -> PKG_CUSTOMER.LOAD
PKG_BATCH.RUN_BATCH -> PKG_ORDER.LOAD
PKG_CUSTOMER.LOAD -> PKG_LOG.WRITE_LOG
```

## Limitations

This is a source-level approximation. Calls performed through `EXECUTE IMMEDIATE`, synonyms, dynamic package names or framework dispatch are not guessed.

## Oracle Dev Tools family

This repository is part of the **Oracle Dev Tools** suite: small, composable developer utilities designed around Oracle Database 19c, 23ai and 26ai.

| Area | Tools |
|---|---|
| Foundation | [ora-core](https://github.com/raoulmunet/ora-core) |
| SQL analysis | [ora-impact](https://github.com/raoulmunet/ora-impact) · [ora-plan](https://github.com/raoulmunet/ora-plan) · [ora-lineage](https://github.com/raoulmunet/ora-lineage) · [ora-lint](https://github.com/raoulmunet/ora-lint) · [ora-sql-diff](https://github.com/raoulmunet/ora-sql-diff) · [ora-sql-complexity](https://github.com/raoulmunet/ora-sql-complexity) · [ora-join-viz](https://github.com/raoulmunet/ora-join-viz) · [ora-bind](https://github.com/raoulmunet/ora-bind) |
| Data & operations | [ora-doc](https://github.com/raoulmunet/ora-doc) · [ora-data-quality](https://github.com/raoulmunet/ora-data-quality) · [ora-csv-loader](https://github.com/raoulmunet/ora-csv-loader) · [ora-etl-log](https://github.com/raoulmunet/ora-etl-log) · [ora-migration-check](https://github.com/raoulmunet/ora-migration-check) · [ora-errors](https://github.com/raoulmunet/ora-errors) · [ora-schema-explorer](https://github.com/raoulmunet/ora-schema-explorer) |
| PL/SQL analysis | [ora-exception-flow](https://github.com/raoulmunet/ora-exception-flow) · [ora-call-graph](https://github.com/raoulmunet/ora-call-graph) · [ora-dead-code](https://github.com/raoulmunet/ora-dead-code) |

## License

MIT.
