class BSTNode(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left

    def __repr__(self):
        """Debugging-friendly representation."""

        return "<BinaryNode %s>" % self.data

    def add_child(self, new_data):
        """Add child in BST"""

        if new_data >= self.data:
            if not self.right:
                self.right = BSTNode(new_data)
            else:
                self.right.add_child(new_data)

        else:
            if not self.left:
                self.left = BSTNode(new_data)
            else:
                self.left.add_child(new_data)


    def get_children(self):
        """Print children of this node"""

        self.children = []
        if self.left:
            self.children.append(self.left)
        if self.right:
            self.children.append(self.right)

        
    def search(self, value):
        """Search for value in BST"""

        current = self

        while current:
            if current.data == value:
                return current

            elif current.data > value:
                current = current.left

            elif current.data < value:
                current = current.right

    def remove(self, value):
        pass


    def print_bfs(self):
        """Print BST in Breadth First Search Order, divided by levels"""

        current_level = [self]
        while current_level:
            next_level = []
            for node in current_level:
                print node.data,
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            print "\n"
            current_level = next_level


    def print_dfs(self):
        """Print BST in Depth First Search Order"""
        to_visit = [self]
        result = []
        while to_visit:
            current = to_visit.pop()
            result.append(current)

            current.get_children()

            if current.children:
                to_visit.extend(current.children)

        return result







t = BSTNode(8)
t.add_child(3)
t.add_child(10)
t.add_child(9)
t.add_child(2)
t.add_child(5)
t.add_child(4)
t.add_child(6)

"""
             8 
          /     \
         3        10
        / \      /  
       2   5    9
          / \
         4   6
"""


