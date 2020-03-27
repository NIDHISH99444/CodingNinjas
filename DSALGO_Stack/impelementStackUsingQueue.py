from _collections import  deque
class MyStack(object):

    def __init__(self):
        self.stack=deque([])


    def push(self, x):
        self.stack.append(x)

    def pop(self):
        for i in range(len(self.stack)-1):
            self.stack.append(self.stack.popleft())
        return self.stack.popleft()

    def top(self):
        return self.stack[-1]
    def empty(self):
        return len(self.stack)==0

stack =MyStack()

stack.push(1)
stack.push(2)
stack.push(3)
print("Popped ele-->",stack.pop())
print("stack top-->",stack.top())
print("Popped ele-->",stack.pop())
print("stack top-->",stack.top())
print("Is stack empty-->",stack.empty())