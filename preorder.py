class Demo:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Demo(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Demo(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
            
    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res
    
root = Demo(30)
root.insert(15)
root.insert(14)
root.insert(1)
root.insert(20)
root.insert(35)
root.insert(32)
root.insert(11)
root.insert(42)

print(root.preorderTraversal(root))
