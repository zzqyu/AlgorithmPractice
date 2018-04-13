class BSTree:
    def __init__(self, data=None, left = None, right = None):
        self.left = left
        self.right = right
        self.data = data
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def setData(self, data):
        self.data = data;
    def getData(self):
        return self.data
    def TPrint(self, d, preD):
        if self.right != None:
            self.right.TPrint(d+1, preD)
        print(" "*d*4, self.data)
        if self.left != None:
            self.left.TPrint(d+1, preD)
        
            


##테스트코드
if __name__ == "__main__" :
    bst=BSTree(4, BSTree(2,BSTree(1), BSTree(3)), BSTree(6, BSTree(5), BSTree(7)))
    bst.TPrint(0, 0);