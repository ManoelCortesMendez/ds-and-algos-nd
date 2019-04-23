class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        return [(edge.value, edge.node_from.value, edge.node_to.value) for edge in self.edges]

    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indecies of the outer list represent
        "value of from node".
        Each section in the list will store a list
        of tuples that looks like this:
        (Value of To Node, Edge Value)"""
        
        # Get maximum node value
        max_index = max([node.value for node in self.nodes])
        
        # Initialize list long enough to reach max_index
        adjacency_list = [None] * (max_index+1)

        # Iterate over all edges
        for edge in self.edges:

            from_val = edge.node_from.value # Get node from value
            to_val = edge.node_to.value # Get node to value
            edge_val = edge.value # Get edge value

            # Store to and edge values at from value index
            # If there's already content stored at index...
            if adjacency_list[from_val]:
                # Append new content
                adjacency_list[from_val].append((to_val, edge_val))
            else:
                # Else, assign new content as a list
                adjacency_list[from_val] = [(to_val, edge_val)]
        
        # Return list of (to value, edge value) tuples indexed by from value
        return adjacency_list
    
    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""

        # Get dimension of future matrix
        dim = max([node.value for node in self.nodes])

        # Initialize square matrix of zeros
        # Matrix is square and indexes by from, to node values
        adjacency_matrix = [[0 for _ in range(dim+1)] for _ in range(dim+1)]

        # Insert edge value at the from, to coordinates
        # That is, fully identify each "from, edge, to" triplet
        for edge in self.edges:
            row = edge.node_from.value
            col = edge.node_to.value
            val = edge.value

            adjacency_matrix[row][col] = val

        # Return matrix of edge values indexed by from, to node values
        return adjacency_matrix

graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)
# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
print graph.get_edge_list()
# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
print graph.get_adjacency_list()
# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print graph.get_adjacency_matrix()