class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Stack:
    def __init__(self,head,size):
        self.head=None
        self.size=0

    def __str__(self,value):
        self.value=value

    def add(self):
        print(self.value)
#     def __isEmpty__(self):

#     def push(self,value):
#         new_node=Node(value)
#         if self.head:
#             new_node.next=self.head
#         self.head=new_node
#         self.size=self.size + 1

#     def traverseAndPrint(self):
#         current=self.head
#         while current is not None:
#             print(current.value)
#             current=current.next

#     def peek(self):
#         if self.head is None:
#             return "Stack is empty"
#         else:
#             return self.head.value

#     def pop(self):
        


    


# mystack=Stack()
# mystack.push("A")
# mystack.push("B")
# mystack.push("C")
# print(mystack.head.value)

# print("LinkedList:")
# mystack.traverseAndPrint()

# print("Peek: ",mystack.peek())
mystr=Stack(10)
mystr.add()