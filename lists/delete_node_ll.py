def delete_ll_node(node):
    """Given a node, delete that node from LL"""
    node.val = node.next.val
    node.next = node.next.next