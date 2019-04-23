class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        """Initiate recursive insert"""
        self.recurse_insert(self.root, new_val)

    def recurse_insert(self, node, new_val):
        """Recursively traverse tree and insert new value"""
        # If new value is smaller than node value...
        if new_val < node.value: 
            if node.left: # ... And if there's a left child...
                self.recurse_insert(node.left, new_val) # Insert recurse left
            else:
                node.left = Node(new_val) # Else, append node as left child
        # If new value is larger than node value...
        else:
            if node.right: # ... And if there's a right child...
                self.recurse_insert(node.right, new_val) # Insert recurse right
            else:
                node.right = Node(new_val) # Else, append node as right child
    
    def search(self, find_val):
        """Initiate recursive search"""
        return self.recurse_search(self.root, find_val)
    
    def recurse_search(self, node, find_val):
        # If current node matches value...
        if node.value == find_val:
            return True # ... value is in tree, so return true
        # Elif, if value is smaller and there's a left node...
        elif node.left and find_val < node.value:
            # Recursively search value in left node
            return self.recurse_search(node.left, find_val)
        # Elif, if value is greater and there's a right node...
        elif node.right and node.value < find_val:
            # Recursively search value in right node
            return self.recurse_search(node.right, find_val)
        # Else, value isn't in node, and there are no more children
        return False # So, return false
    
    # Helper functions (for debugging)
    def print_tree(self):
        """Initiate recursive traversal of tree, and return full path"""
        return self.recurse_print_tree(self.root)
    
    def recurse_print_tree(self, node):
        # Initialize string to store values of nodes visited        
        nodes_visited = ""

        # Add current node value to string
        nodes_visited += str(node.value)
        # If there's a left child...
        if node.left:
            # ... add left node value to string
            nodes_visited += self.recurse_print_tree(node.left)
        # If there's a right child...
        if node.right:
            # ... add right node value to string
            nodes_visited += self.recurse_print_tree(node.right)

        # Return full string of nodes visited
        return nodes_visited

    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Print tree (for debugging)
# print tree.print_tree()

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)