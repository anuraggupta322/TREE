class Node:
    def __init__(self,key):
        self.value=key
        self.left=None
        self.right=None

def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.value==key:
            return root
        else if(root.value<key):
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value,end="")
        inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value,end=" ")
def preorder(root):
    if root:
        print(root.value,end="")
        preorder(root.left)
        preorder(root.right)
