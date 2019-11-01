class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue(object):
    def __init__(self):
        self.first = None
        self.last = None

    def put(self, data):
        if not self.first:
            self.first = Node(data, None)
            self.last = self.first
            return
        newNode = Node(data, None)
        next = self.last
        while next.next != None:
            next = next.next
        next.next = newNode

    def get(self):
        save = self.first.data
        saveNext = self.first.next
        del self.first
        self.first = saveNext
        return save
