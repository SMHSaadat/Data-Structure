class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.Lchild = None
        self.Rchild = None

class BST:
    def __init__(self):
        self.root = None
        self.l = list()
        
    def insert(self, data):
        self.l.append(data)
        if self.root is None:
            self.root = BinaryNode(data)
        else:
            return self.recins(self.root, data)

    def recins(self, root, data):
        if data > root.data:
            if root.Rchild is None:
                root.Rchild  = BinaryNode(data)
            else:
                self.recins(root.Rchild, data)
        else:
            if root.Lchild is None:
                root.Lchild = BinaryNode(data)
            else:
                self.recins(root.Lchild, data)
                
    def show_list(self):
        print(self.l)
        return(self.l)
    
    def search(self, data):
        return self.inorder(self.root, data)
    
    def inorder(self, root, data):
        if root is None:
            return -1
        elif root.data == data:
            return root
        else:
            if data > root.data:
                return self.inorder(root.Rchild)
            return self.inorder(root.Lchild)

    def display(self):
        return self.postorder(self, self.root)
    
    def postorder(self, root):
        if root is None:
            return None
        else:
            self.postorder(root.Lchild)
            self.postorder(root.Rchild)
            print(root.data, end=' ')
                   

# write a function that takes a list from input and returns the bst tree in the output

def quize(l):
    result = BST()
    for i in l:
        result.insert(i)
        