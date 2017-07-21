def is_same_bst(node1, node2):
    """Are these trees the same tree?"""

    #Base case: we reach node after leaf nodes and return True as we're done
    if node1 is None and node2 is None:
        return True

    #If only one is None, that means they are not the same
    if node1 is None or node2 is None:
        return False

    if node1.val == node2.val:
        return validate_children(node1.left, node2.left) and validate_children(node1.right, node2.right)

    return node1 is node2


def is_same_tree_short(node1, node2):

    if node1 and node2:
        return node1.val==node2.val and is_same_tree_short(node1.left, node2.left) and is_same_tree_short(node1.right, node2.right)

    return node1 is node2