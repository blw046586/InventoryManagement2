# === warehouse/layout.py ===
import networkx as nx

class WarehouseGraphManager:
    def __init__(self):
        self.graph = nx.Graph()

    def add_zone(self, zone):
        self.graph.add_node(zone)

    def add_path(self, from_zone, to_zone, distance):
        self.graph.add_edge(from_zone, to_zone, weight=distance)

    def shortest_path(self, start, end):
        return nx.shortest_path(self.graph, start, end, weight='weight')

