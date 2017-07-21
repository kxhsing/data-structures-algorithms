def is_symmetric_tree(root):
    """Are branches of tree symmetric?"""

    if root is None:
        return True
    else:
        return is_mirror(root.left, root.right)

def is_mirror(left, right):

    if left is None and right is None:
        return True

    #If one of them is None, that means they are not the same shape
    if left is None or right is None:
        return False

    #Check outer branches
    outer = is_mirror(left.left, right.right)
    inner = is_mirror(left.right, right.left)

    return outer and inner

    