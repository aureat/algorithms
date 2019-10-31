class Node(object):
    def __init__(self,data, next):
        self.data = data
        self.next = next

class Queue(object):
    def __init__(self):
        self.last = None
        self.foll = None

    def is_empty(self):
        if self.last is None:
            return True
        return False

    def put(self, data):
        if self.is_empty():
            self.last = Node(data, None)
            self.foll = self.last
            return
        self.foll = Node(data, self.foll)

    def get(self):
        save = self.last
        next = self.foll
        if next == self.last:
            next.next = None
            self.foll = self.last = None
            return save
        while next.next != self.last:
            next = next.next
        del self.last
        self.last = next
        next.next = None
        return save

    def get_data(self):
        data = []
        next = self.foll
        while next is not None:
            data.append(next.data)
            next = next.next
        return data
