import threading
import time

# Simple Queue class
class Queue:
    def __init__(self):
        self.orders = []

    def enqueue(self, item):
        self.orders.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.orders.pop()

    def is_empty(self):
        return len(self.orders) == 0

# Create queue and order list
food_queue = Queue()
orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']

# Thread 1: Place order
def place_orders():
    for order in orders:
        print(f"Placing order: {order}")
        food_queue.enqueue(order)
        time.sleep(0.5)

# Thread 2: Serve order
def serve_orders():
    time.sleep(1)  # Delay start
    while True:
        if not food_queue.is_empty():
            order = food_queue.dequeue()
            print(f"Serving order: {order}")
        else:
            print("Waiting for orders...")
        time.sleep(2)

# Start threads
t1 = threading.Thread(target=place_orders)
t2 = threading.Thread(target=serve_orders)

t1.start()
t2.start()
