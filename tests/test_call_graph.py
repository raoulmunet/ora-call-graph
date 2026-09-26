from ora_call_graph import scan_source

SQL="""CREATE OR REPLACE PACKAGE BODY pkg_batch AS
PROCEDURE run_batch IS
BEGIN
  pkg_customer.load(1);
  pkg_log.write_log('done');
END;
PROCEDURE helper IS
BEGIN
  pkg_log.write_log('helper');
END;
END;"""

def test_edges():
    e=scan_source(SQL)
    pairs={(x.caller,x.callee) for x in e}
    assert ("PKG_BATCH.RUN_BATCH","PKG_CUSTOMER.LOAD") in pairs
    assert ("PKG_BATCH.RUN_BATCH","PKG_LOG.WRITE_LOG") in pairs
