class Stack:
    def __init__(self):
        self.stack=[]

    def isEmpty(self):
        return len(self.stack)==0
    
    def push(self,element):
        self.stack.extend(element)

    def pop(self):
        if self.isEmpty is True:
            return "stack is empty"
        else:
            self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            print(self.stack[-1])

    def size(self):
        print(len(self.stack))
    
s1=Stack()
s1.push((10,20,30))
print(s1.stack)
s1.pop()
print(s1.stack)
s1.peek()
s1.size()


