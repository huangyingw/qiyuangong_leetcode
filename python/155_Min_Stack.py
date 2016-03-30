class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if len(self.min_stack) == 0 or x <= self.min_stack[-1]:
            self.min_stack.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.stack) > 0:
            last = self.stack[-1]
            if len(self.min_stack) > 0 and last == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        return None


    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min_stack) > 0:
            return self.min_stack[-1]
        else:
            if len(self.stack) > 0:
                return self.stack[-1]
            return None
