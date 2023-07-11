class MyQueue:

    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = 0

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        elePop = self.queue[0]
        if len(self.queue) != 0:
            self.queue.pop(0)
            
        return elePop
    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        if self.queue == []:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.peek()
param_3 = obj.pop()
param_4 = obj.empty()
print(param_2, param_3, param_4)

# obj = MyQueue()
# obj.push(1)
# param_3 = obj.pop()
# param_4 = obj.empty()
# print(param_3, param_4)