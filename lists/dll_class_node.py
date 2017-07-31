class Node(object):
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

    def __repr__(self):
        return "<Node {}>".format(self.data)


class DoublyLinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.tail = None

    def push(self, data):
        """Add node to front of DLL"""

        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node

        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
            self.head.previous = None

    def pop(self):
        """Remove node from end of DLL"""

        if self.tail:
            if self.tail.previous:
                self.tail = self.tail.previous
                if self.tail.previous is None:
                    self.head = self.tail
                self.tail.next = None

            elif not self.tail.previous:
                self.head = None
                self.tail = None

        else:
            return "No node to pop"


    def remove(self, node):
        """Remove node and connect previous and next nodes together"""

        if node.next and node.previous:
            next_node = node.next
            previous_node = node.previous

            previous_node.next = next_node
            next_node.previous = previous_node

            node.next = node.previous = None #Make this node free standing

        elif node.next: #we're removing the current head node
            self.head = node.next

        elif node.previous: #we're removing current last node
            self.tail = node.previous
            self.tail.next = None
            # self.tail.previous = second_to_last
            # second_to_last = self.tail.previous.previous


# Creating DLL: B -> C
b = Node('b')
c = Node('c')
b.next = c
c.previous = b
c.next = None
dll = DoublyLinkedList()

dll.head = b
dll.tail = c
dll.push('a') # Push node A to front of DLL, make it head
# DLL: A -> B -> C

dll.pop() # Pop node C
# DLL: A -> B

dll.remove(b)
# DLL: A










