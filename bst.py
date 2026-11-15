class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Bst:
    def __init__(self):
        self.root=None

    def insert(self,value):
        new_node=Node(value)
        temp=self.root
        if temp.root is None:
            self.root=new_node
            return
        else:
            if new_node.data<temp.root:
                if temp.left is None:
                    temp.left=new_node
                else:
                    while temp is not None:
                        if new_node.data<temp.root:
                            temp=temp.left
                        else:
                            temp=temp.right
                    temp.next=new_node

    def inorder()

