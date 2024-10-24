# rule_engine/ast.py

class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # "operator" or "operand"
        self.left = left            # Left child node
        self.right = right          # Right child node
        self.value = value          # Value for operands, like {"attribute": "age", "operator": ">", "value": 30}
    
    def __repr__(self):
        return f"Node({self.node_type}, {self.left}, {self.right}, {self.value})"


    def __repr__(self):
        return f"Node({self.node_type}, {self.left}, {self.right}, {self.value})"

# Test the Node class
if __name__ == "__main__":
    # Creating a sample node to test
    left_child = Node('operand', value='age > 30')
    right_child = Node('operand', value='department = "Sales"')
    root = Node('operator', left=left_child, right=right_child, value='AND')

    print(root)  # Should print the structure of the root node
