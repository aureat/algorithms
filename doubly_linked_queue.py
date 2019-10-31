class Node(object):
    def __init__(self, data, next, before):
        self.data = data
        self.next = next
        self.before = before

# Doubly-linked Queue (DEQUE)
class Queue(object):
    def __init__(self):
        self.first = None
        self.last = None

    def put(self, data):
        if not self.first:
            self.first = Node(data, None, None)
            self.last = self.first
            return
        newNode = Node(data, None, None)
        self.last.next = newNode
        self.last.next.before = self.last
        self.last = self.last.next

    def get(self):
        save = self.first.data
        saveNext = self.first.next
        del self.first
        if saveNext:
            saveNext.before = None
            self.first = saveNext
        else:
             self.first = None
        return save

    def push(self, lst):
        for arg in lst:
            self.put(arg)

    def get_data(self):
        data = []
        next = self.first
        while next is not None:
            data.append(next.data)
            next = next.next
        return data

    # def __bool__(self):
    #     if self.first is not None:
    #         return True
    #     return False

    def __nonzero__(self):
        if self.first is not None:
            return True
        return False

# q = Queue()
# q.put(12)
# q.put(24)
# q.put(34)
# q.put(53)
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# if q:
#     print('yes')
