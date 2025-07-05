# Stack class from tutorial
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

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

# Function to check balanced parentheses
def is_balanced(expression):
    stack = Stack()
    opening = "({["
    closing = ")}]"
    matches = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty():
                return False
            if stack.pop() != matches[char]:
                return False

    return stack.is_empty()


print(is_balanced("({a+b})"))                  
print(is_balanced("))((a+b}{"))               
print(is_balanced("((a+b))"))                 
print(is_balanced("))"))                      
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))     
