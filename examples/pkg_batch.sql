CREATE OR REPLACE PACKAGE BODY pkg_batch AS
  PROCEDURE run_batch IS
  BEGIN
    pkg_customer.load_customers();
    pkg_order.load_orders();
    pkg_log.write_log('Batch complete');
  END run_batch;
END pkg_batch;
/
