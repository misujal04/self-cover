class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
        self.size=0

    def isEmpty(self):
        return self.size == 0

    def push(self,value):
        new_node=Node(value)
        if self.head:
            new_node.next=self.head
        self.head=new_node
        self.size=self.size + 1

    def traverseAndPrint(self):
        current=self.head
        while current is not None:
            print(current.value)
            current=current.next

    def peek(self):
        if self.head is None:
            return "Stack is empty"
        else:
            return self.head.value

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        popped_node=self.head
        self.head=self.head.next
        self.size=self.size-1
        return popped_node.value
        


    


mystack=Stack()
mystack.push("A")
mystack.push("B")
mystack.push("C")
print(mystack.head.value)

print("LinkedList:")
mystack.traverseAndPrint()

print("Peek: ",mystack.peek())
print("pop: ",mystack.pop())
mystack.traverseAndPrint()
print("isEmpty:", mystack.isEmpty())
print("Size",mystack.size)
