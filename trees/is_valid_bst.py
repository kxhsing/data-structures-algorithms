def is_valid_bst(root):

    def check_children(node, lt, gt):
        """
        lt: children left of node must always be less than this value
        gt: children right of node must always be greater than this value
        """

        if node is None:
            return

        if (lt is not None and node.data > lt) or (gt is not None node.data < gt):
            raise ValueError

        check_children(node.left, node.data, gt)
        check_children(node.right, lt, node.data)


    try:
        check_children(root, None, None)
        return True

    except ValueError:
        return False

