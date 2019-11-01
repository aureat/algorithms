class Node(object):
    def __init__(self, data, next, priority = 0):
        self.data = data
        self.next = next
        self.priority = priority

class PriorityQueue(object):
    def __init__(self):
        self.first = None
        self.counter = 0

    def __len__(self):
        return self.counter

    def put(self, data, priority = 0):
        self.counter += 1
        if not self.first:
            self.first = Node(data, None, priority)
            return
        newNode = Node(data, None, priority)
        next = self.first
        while next.next != None:
            next = next.next
        next.next = newNode

    def getMax(self):
        helper_node = self.first
        max = helper_node.priority
        f = 0
        for _ in range(self.counter - 1):
            if helper_node.next.priority > max:
                max = helper_node.next.priority
                f = 1
            helper_node = helper_node.next
        considered = self.first
        self.counter -= 1
        if f and self.first.priority != max:
            considered = self.first
            while considered.next != None and considered.next.priority != max:
                considered = considered.next
            node = considered.next
            considered.next = considered.next.next
            return node.data
        node = self.first
        self.first = self.first.next
        return node.data

    def getMin(self):
        helper_node = self.first
        min = helper_node.priority
        f = 0
        for _ in range(self.counter - 1):
            if helper_node.next.priority < min:
                min = helper_node.next.priority
                f = 1
            helper_node = helper_node.next
        considered = self.first
        self.counter -= 1
        if f and self.first.priority != min:
            considered = self.first
            while considered.next != None and considered.next.priority != min:
                considered = considered.next
            node = considered.next
            considered.next = considered.next.next
            return node.data
        node = self.first
        self.first = self.first.next
        return node.data

    def get_data(self):
        data = []
        next = self.first
        while next is not None:
            data.append((next.data, next.next))
            next = next.next
        print(data)

# q = PriorityQueue()
# q.put(12,0)
# q.put(24,0)
# q.put(34,0)
# q.put(53,0)
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
