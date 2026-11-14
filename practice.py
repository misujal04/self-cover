class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head=None
        self.size=0

    def push(self,value):
        new_node=Node(value)
        if self.head:
            new_node.next=self.head
        self.head=new_node
        self.size=self.size+1

    def traverse(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next

    def peek(self):
        if self.head is None:
            return "Stack is Empty"
        else:
            return (self.head.data)

    def pop(self):
        if self.head is None:
            return "Stack is Empty"
        else:
            pop_node=self.head
            self.head=self.head.next
            self.size=self.size-1
            return pop_node.data

    def isEmpty(self):
        if sttack.head:
            return False
        else:
            return True

    def Size(self):
        return self.size

sttack=Stack()
sttack.push(10)
sttack.push(20)
sttack.push(30)
sttack.push(40)
sttack.push(50)
sttack.traverse()
print("Peek : ",sttack.peek())
print("Pop : ",sttack.pop())
sttack.traverse()
print("Is Stack empty",sttack.isEmpty())
print("Size of Stack ",sttack.Size())