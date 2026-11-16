class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.length=0

    def enqueue(self,value):
        new_node=Node(value)
        if self.rear is None:
            self.rear=self.front=new_node
            self.length+=1
        else:
            self.rear.next=new_node
            self.rear=new_node
            self.length+=1

    def display(self):
        temp=self.front
        while temp is not None:
            print(temp.data,end="-->")
            temp=temp.next
        print("None")
        
    def dequeue(self):
        if self.front is None:
            return "Queue is Empty"
        temp=self.front
        self.front=temp.next
        self.length-=1
        if self.front is None:
            self.rear=None
            print(temp.data)

    def peek(self):
        if self.front is None:
            return "queue is empty"
        return(self.front.data)

    def length(self):
        if self.front is None:
            return "queue is empty"
        return(self.length)

    def IsEmpty(self):
        if self.front is None:
            return "True"
        return "False"
     


s1=Queue()
s1.enqueue(10)
s1.enqueue(20)
s1.enqueue(30)
s1.display()
s1.dequeue()
print("After dequeue the queue :")
s1.display
s1.peek()
print("length of queue",s1.length)
print("Isempty",s1.IsEmpty())
