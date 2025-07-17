class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, mode="both"):
        # Decide what to print based on mode
        if mode == "name":
            value = self.name
        elif mode == "designation":
            value = self.designation
        else:
            value = f"{self.name} ({self.designation})"

        # Print with indentation
        indent = " " * self.get_level() * 3
        prefix = indent + "|__" if self.parent else ""
        print(prefix + value)

        for child in self.children:
            child.print_tree(mode)

# Function to build company hierarchy
def build_management_tree():
    # CEO
    ceo = TreeNode("Nilupul", "CEO")

    # CTO subtree
    cto = TreeNode("Chinmay", "CTO")
    infra_head = TreeNode("Vishwa", "Infrastructure Head")
    infra_head.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))

    cto.add_child(infra_head)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    # HR subtree
    hr_head = TreeNode("Gels", "HR Head")
    hr_head.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

    # Build full tree
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo

# Main function
if __name__ == '__main__':
    root_node = build_management_tree()
    print("\nName Only:\n")
    root_node.print_tree("name")

    print("\nDesignation Only:\n")
    root_node.print_tree("designation")

    print("\nName and Designation:\n")
    root_node.print_tree("both")
