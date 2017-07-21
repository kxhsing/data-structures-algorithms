class Node(object):
    def __init__(self, data, children = None):
        self.data = data
        self.children = children or []

    def speak(self):
        print "hello!"


def count_nodes(node):
    if node is None:
        return

    count = 1

    for child in node.children:
        count += count_nodes(child)

    return count


def count_subnodes(node):
    if node is None:
        return 

    def _count_nodes(node):

        count = 1

        for child in node.children:
            count += _count_nodes(child)

        return count

    return _count_nodes(node) - 1


leaf = Node('leaf', [Node('seed', []), Node('petal', [])])
tree = Node('tree', [Node('flower', []), leaf])

