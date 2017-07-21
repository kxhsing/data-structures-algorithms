class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self, head):
        self.head = head
        self.tail = None

    def append(self, data):
        """Create new node with data, then add to LL.
        If head is nonexistent, make new node head. 
        If tail is not none, add to end of list"""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node
        
        self.tail = new_node

    def remove(self, data):
        """Remove a node with given data"""

        if self.head and self.head.data==data:
            self.head = self.head.next
            if self.head is None: #did we delete the only node in LL?
                self.tail = None

        current = self.head

        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                return
            else:
                current = current.next

    def search(self, data):
        """Search if data is in LL"""

        current = self.head

        while current:
            if current.data == data:
                return True
            else:
                current = current.next

        return False 





ll = LinkedList()
ll.append("apple")
ll.append("berry")
ll.append("cherry")
ll.append("dragonfruit")
ll.append("elderberry")













