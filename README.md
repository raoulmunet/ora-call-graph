# ora-call-graph

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

## License

MIT.
