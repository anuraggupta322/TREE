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
def Search(root,key):
    if root is None or root.value==key:
        return root
    elif (root.value<key):
        Search(root.right,key)
    Search(root.left,key)