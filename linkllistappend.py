class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def append(head,data):
    new_node=Node(data)
    if head is None:
        return new_node
    current=head
    while current.next is not None:
        current=current.next
    current.next=new_node
    return head
    

n=int(input("Enter the numbers of nodes you want"))
head=None
for i in range(n):
    data=int(input("Enter the data of node"))
    head=append(head,data)

current=head
while current is not None:
    print(current.data)
    current=current.next
    
    