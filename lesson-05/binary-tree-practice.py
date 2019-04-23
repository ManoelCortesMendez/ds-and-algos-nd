class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""

        # Initiate recursive search starting at root
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""

        # Get string of nodes visited recursively
        nodes_visited = self.preorder_print(self.root, "")

        # Separate each node with a dash and return
        return '-'.join(list(nodes_visited))

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""

        # Define base case
        if start.value == find_val: return True
        
        # If node is parent
        if start.left or start.right:
            
            # Recurse to see if val is in left or right tree
            left_match = self.preorder_search(start.left, find_val)
            right_match = self.preorder_search(start.right, find_val)
            
            # If there's a match on either side, return true
            return left_match or right_match

        # Else, return False
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""

        # Add current node value to string of nodes visited
        nodes_visited = str(start.value)

        # If current node has left child, recurse left
        if start.left:
            nodes_visited += self.preorder_print(start.left, traversal)

        # If current node has right child, recurse right
        if start.right:
            nodes_visited += self.preorder_print(start.right, traversal)

        # Return string of nodes visited
        return nodes_visited


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()