# === analytics/reports.py ===
import pandas as pd

class ReportGenerator:
    def __init__(self, inventory_manager):
        self.inventory = inventory_manager

    def stock_report(self):
        data = [
            {"SKU": sku, **info}
            for sku, info in self.inventory.sku_map.items()
        ]
        df = pd.DataFrame(data)
        return df.groupby('category')['quantity'].sum()
