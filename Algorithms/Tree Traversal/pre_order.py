from . import root


def pre_order(root):
    if root:
        print(root.nodedata)
        pre_order(root.childleft)
        pre_order(root.childright)


pre_order(root)
