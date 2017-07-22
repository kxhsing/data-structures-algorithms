class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self, data):
        self.stack.pop()

    def peek(self, data):
        return self.stack[-1]


class Queue(object):
    def __init__(self):
        self.queue = []
        self.transfer_list = []

    def transfer(self):
        """If queue is empty, check to see if transfer list has items. If so
        continue transferring to queue until empty"""
        
        if len(self.queue) == 0:
            if self.transfer_list:
                while len(self.transfer_list) > 0:
                    self.queue.append(self.transfer_list.pop())
            else:
                return "Nothing left in queue"

    def push(self, data):
        self.transfer_list.append(data)

    def peek(self):
        self.transfer()
        return self.queue[-1]

    def pop(self):
        self.transfer()
        self.queue.pop()
