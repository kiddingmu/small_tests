class Node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None

def binary_insert(root, node):
    """
    if not root:
        root = node
    else:
        if root.val > node.val:
            if root.left_child == None:
                root.left_child = node
            else:
                binary_insert(root.left_child, node)
        else:
            if root.right_child == None:
                root.right_child = node
            else:
                binary_insert(root.right_child, node)
    """
    if root is None:
        return node
    if root.val > node.val:
        root.left_child = binary_insert(root.left_child, node)
    else:
        root.right_child = binary_insert(root.right_child, node)
    return root

def in_order_print(root):
    if not root:
        return
    in_order_print(root.left_child)
    print root.val
    in_order_print(root.right_child)

def pre_order_print(root):
    if not root:
        return
    print root.val
    pre_order_print(root.left_child)
    pre_order_print(root.right_child)

def main():
    r = Node(3)
    binary_insert(r, Node(7))
    binary_insert(r, Node(1))
    binary_insert(r, Node(5))
    binary_insert(r, Node(1))
    binary_insert(r, Node(2))

    print "in order:"
    in_order_print(r)

    print "pre order"
    pre_order_print(r)

if __name__ == "__main__":
    main()
