class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, val):
        if val == self.data:
            return  # No duplicates in BST

        if val < self.data:
            if self.left:
                self.left.add_child(val)
            else:
                self.left = BinarySearchTreeNode(val)
        else:
            if self.right:
                self.right.add_child(val)
            else:
                self.right = BinarySearchTreeNode(val)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    # 1. Find Minimum
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    # 2. Find Maximum
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    bst = build_tree(numbers)

    print("In-order Traversal:", bst.in_order_traversal())
    print("Min value:", bst.find_min())
    print("Max value:", bst.find_max())
    print("Sum of all values:", bst.calculate_sum())
    print("Post-order Traversal:", bst.post_order_traversal())
    print("Pre-order Traversal:", bst.pre_order_traversal())
