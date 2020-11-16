from . import root


def post_order(root):
    if root:
        post_order(root.childleft)
        post_order(root.childright)
        print(root.nodedata)


post_order(root)
