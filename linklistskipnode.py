class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
a=Node(10)
ab=Node(15)
b=Node(20)
c=Node(30)
head=a
a.next=ab
ab.next=b
b.next=c
move=head


while(move!=None):
        
    print(move.data)
    if(move.data==15):
        move=move.next.next
    else:
        move=move.next

    
    
