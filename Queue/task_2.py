# Custom Queue class
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.insert(0, value)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def front(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

# Function to generate binary numbers from 1 to n
def generate_binary_numbers(n):
    q = Queue()
    q.enqueue("1")

    for _ in range(n):
        front = q.front()
        print(front)  # Print the binary number
        q.enqueue(front + "0")
        q.enqueue(front + "1")
        q.dequeue()  # Remove the printed number

# Call the function to print binary numbers from 1 to 10
generate_binary_numbers(10)
