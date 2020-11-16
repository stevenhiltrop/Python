from . import root


def in_order_traversal(root):
    if root:
        in_order_traversal(root.child_left)
        print(root.node_data)
        in_order_traversal(root.child_right)


in_order_traversal(root)
