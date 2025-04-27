# === tests/test_order.py ===
def test_order_processing():
    from order.processor import OrderProcessor
    op = OrderProcessor()
    op.add_order({"order_id": 1}, urgent=True)
    assert op.process_next_order()["order_id"] == 1
