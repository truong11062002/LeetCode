class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, ele):
        if len(self.min_stack) != 0:
            if ele <= self.min_stack[-1]:
                self.min_stack.append(ele)
        else:
            self.min_stack.append(ele)
        self.stack.append(ele)

    def pop(self):
        if len(self.stack) != 0:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self):
        if len(self.stack) != 0:
            return self.stack[-1]

    def getMin(self):
        if (self.min_stack) != 0:
            return self.min_stack[-1]
        else:
            return -1


# Your MinStack object will be instantiated and called as such:
obj = MinStack()

obj.push(-2)
obj.push(0)
obj.push(-3)
param_2 = obj.getMin()
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()

print(param_2)
print(param_3)
print(param_4)