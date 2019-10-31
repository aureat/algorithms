class BinaryNode(object):

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if data < self.data:
            if not self.leftChild:
                self.leftChild = BinaryNode(data)
            else:
                self.leftChild.insert(data)
        else:
            if not self.rightChild:
                self.rightChild = BinaryNode(data)
            else:
                self.rightChild.insert(data)

    def getMin(self):
        if self.leftChild is None:
            return self.data
        else:
            return self.leftChild.getMin()

    def getMax(self):
        if self.rightChild is None:
            return self.data
        else:
            return self.rightChild.getMax()

    def getAll(self, vals):
        if self.leftChild:
            listLeft = []
            listLeft.append(self.leftChild.data)
            self.leftChild.getAll(listLeft)
            vals.append(listLeft)
        if self.rightChild:
            listRight = []
            listRight.append(self.rightChild.data)
            self.rightChild.getAll(listRight)
            vals.append(listRight)
        return vals
