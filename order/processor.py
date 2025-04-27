# === order/processor.py ===
from collections import deque
import heapq

class OrderProcessor:
    def __init__(self):
        self.order_queue = deque()
        self.priority_heap = []

    def add_order(self, order, urgent=False):
        if urgent:
            heapq.heappush(self.priority_heap, (1, order))
        else:
            self.order_queue.append(order)

    def process_next_order(self):
        if self.priority_heap:
            return heapq.heappop(self.priority_heap)[1]
        elif self.order_queue:
            return self.order_queue.popleft()
        return None

