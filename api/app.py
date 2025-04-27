# === api/app.py ===
from fastapi import FastAPI
from inventory.manager import InventoryManager
from order.processor import OrderProcessor

app = FastAPI()

inventory = InventoryManager()
orders = OrderProcessor()

@app.post("/product/add")
def add_product(sku: str, name: str, quantity: int, category: str):
    inventory.add_product(sku, {"name": name, "quantity": quantity, "category": category})
    return {"status": "success"}

@app.post("/order")
def place_order(order_id: int, sku: str, urgent: bool = False):
    orders.add_order({"order_id": order_id, "sku": sku}, urgent)
    return {"status": "queued"}

@app.get("/order/next")
def next_order():
    return orders.process_next_order()
