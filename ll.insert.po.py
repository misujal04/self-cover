class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node

    def display(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next
        print("None")

    def insert(self,value,po):
        new_node=Node(value)
        at=1
        if at==po:
            new_node.next=self.head
            self.head=new_node
        current=self.head
        while current.next is not None:
            prev=current
            current=current.next
            at=at+1
            if at==po:
                temp=current
                prev.next=new_node
                new_node.next=current

            
ll=Linkedlist()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.display()
ll.insert(100,1)
ll.display()
