class Node:
    def __init__(self,value):
        self.data=value
        self.right=None
        self.left=None

class Bst:
    def __init__(self):
        self.root=None
    def insert(self,new_node):
        #new_node=Node(new_node)
        if self.root is None:
            self.root=new_node
        else:
            while True:
                if self.root>=new_node:
                    if self.root.right is None:
                        self.root.right=new_node
                    else:
                        temp=self.root.left is None

        
            

s1=Bst()
s1.insert(Node(10))
print(s1.root.data)
