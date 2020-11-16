class Node:
    def __init__(self, letter):
        self.child_left = None
        self.child_right = None
        self.node_data = letter


# create the nodes for the tree
root = Node('A')
root.child_left = Node('B')
root.child_right = Node('C')
root.child_left.child_left = Node('D')
root.child_left.child_right = Node('E')
