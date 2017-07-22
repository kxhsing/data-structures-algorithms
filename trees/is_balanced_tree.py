def is_balanced_tree(root):
    """Tree is balanced if lowest descendants on left and right side differ 
    in levels of no more than 1"""

    def check_children(node):
        if node is None:
            return 0

        left = check_children(node.left)
        right = check_children(node.right)

        if abs(left - right) > 1:
            raise ValueError()

        else:
            #get max height of node, which is height of deepest descendant + self
            return max(left, right) + 1

    try:
        check_children(root)
        return True

    except ValueError:
        return False