def find_max_depth(root):
    if root is None:
        return 0

    return max(find_max_depth(root.left), find_max_depth(root.right)) + 1


def find_min_depth(root):
    if root is None:
        return 0

    if root.left is None or root.right is None:
        return find_min_depth(root.left) + find_min_depth(root.right) + 1

    return min(find_min_depth(root.left), find_min_depth(root.right)) + 1
    