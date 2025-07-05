# Define the Stack class
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

# Function to reverse a string using stack
def reverse_string(input_str):
    stack = Stack()

    # Push all characters of string into the stack
    for char in input_str:
        stack.push(char)

    # Pop all characters from stack and add to reversed_str
    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str

# Example usage
result = reverse_string("We will conquere COVID-19")
print(result)  # Output: "91-DIVOC ereuqnoc lliw eW"
