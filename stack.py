class Node(object):
    def __init__(self, data):
        self.nextNode = None
        self.data = data

class Stack(object):

    def __init__(self):
        self.head = None
        self.counter = 0

    def push(self, data):
        newNode = Node(data)
        newNode.nextNode = self.head
        self.head = newNode
        self.counter += 1

    def pop(self):
        if self.head:
            data = self.head.data
            nxt = self.head.nextNode
            del self.head
            self.head = nxt
            self.counter -= 1
            return data

    # as opposed to pop and then push the return value: >> peek = stack.pop() >> stack.push(peek) >> print(peek)
    def peek(self):
        if self.head:
            return self.head.data

    # def __bool__(self):
    #     if self.counter > 0:
    #         return True
    #     return False

    def __nonzero__(self):
        if self.counter > 0:
            return True
        return False

    def __len__(self):
        return self.counter

    def getAll(self):
        start = self.head
        text = ''
        while start is not None:
            text += str(start.data) + ' '
            start = start.nextNode
        print(text)
