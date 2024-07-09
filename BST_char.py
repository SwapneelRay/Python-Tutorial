class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None

def newNode(data):
    node= TreeNode(0)
    node.data=data
    node.left=None
    node.right=None
    return(node)

def insert(node,data):
    if(node==None):
        return(newNode(data))
    else:
        if(data<=node.data):
            node.left = insert(node.left,data)
        else:
            node.right = insert(node.right,data)
    return(node)

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

root =None
root = insert(root,"R")
root = insert(root,"A")
root = insert(root,"Z")
root = insert(root,"C")
root = insert(root,"D")
root = insert(root,"E")
root = insert(root,"F")
root = insert(root,"G")
inOrderTraversal(root)

