class MyStack:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
            
    def pop(self) -> int:
        top = 0
        if len(self.stack) != 0:
            top = self.stack[-1]
            self.stack.pop()
            return top
    def top(self) -> int:
        return self.stack[-1]
        
    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        return False

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)

param_2 = obj.top()
param_3 = obj.pop()
param_4 = obj.empty()
print(param_2, param_3, param_4)