
class MinStack:
    def __init__(self):
        self.stack=[]

    def push(self, x):
        if self.stack:
            self.stack.append([x,min(x,self.stack[-1][1])])
        else:
            self.stack.append([x,x])

    def pop(self):
        if self.stack:
            self.stack.pop()


    def top(self):
        if self.stack:
            return self.stack[-1][0]



    def getMin(self):
        if self.stack:
            return self.stack[-1][1]

minStack=MinStack()
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
print("min ele-->",minStack.getMin())
minStack.pop()
print("top ele-->",minStack.top())
print("min ele-->",minStack.getMin())