class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        # Check to see if x or current minimum number is smaller, if x is smaller
        # or there is no current min, set current min to x, then append

        curr_min = self.getMin()
        if curr_min is None or x < curr_min:
            curr_min = x
        self.stack.append((x, curr_min))

        

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][1]       


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()