class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right= None
        
def newNode(data):
    node = TreeNode(0)
    node.data = data
    node.left = None
    node.right = None
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
    
    
def minValue(node):
    if(node.left==None):
        return node.data
    return minValue(node.left)

def maxValue(node):
    if(node.right==None):
        return node.data
    return maxValue(node.right)

root = None
root = insert(root,13)
root = insert(root,7)
root = insert(root,15)
root = insert(root,3)
root = insert(root,8)
root = insert(root,14)
root = insert(root,19)
root = insert(root,18)

print(maxValue(root))
print(minValue(root))

inOrderTraversal(root)
        
    
    