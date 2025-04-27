# === services/restock_worker.py ===
from celery import Celery

app = Celery('restock', broker='redis://redis:6379/0')

@app.task
def restock_item(sku, quantity):
    print(f"Restocking {sku} with {quantity} units.")

