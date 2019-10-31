class Node(object):

    def __init__(self, data):
        self.nextNode = None;
        self.data = data;

    def remove(self, data, previousNode):
        if self.data == data:
            previousNode.nextNode = self.nextNode
            del self.data
            del self.nextNode
        else:
            if self.nextNode is not None:
                self.nextNode.remove(data, self)


class LinkedList(object):

    def __init__(self):
        self.head = None;
        self.counter = 0;

        # dummyNode = Node('BEGIN')
        # dummyNode.nextNode = self.head

    # O(1)
    def size(self):
        return self.counter

    # O(1)
    def insertStart(self, data):

        self.counter += 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            previousNode = self.head
            self.head = newNode
            newNode.nextNode = previousNode

    # O(N)
    def insertEnd(self, data):

        # if not self.head:
        #     insertStart(data)
        #     return

        self.counter += 1
        newNode = Node(data)

        if not self.head:

            self.head = newNode

        else:

            getNode = self.head
            while getNode.nextNode is not None:
                getNode = getNode.nextNode

            getNode.nextNode = newNode

    # O(N) First method of removing an element -- traversing through the node classes
    def remove(self, data):
        if self.head:
            if self.head.data is data:
                self.head = self.head.nextNode
            else:
                actualNode = self.head
                actualNode.remove(data, self.head)
            self.counter -= 1

    # O(N)
    def traverseList(self):
        startNode = self.head
        while startNode is not None:
            print(startNode.data)
            startNode = startNode.nextNode

    # O(N)
    def listSearch(self, k):
        startNode = self.head
        while startNode is not None and startNode.data is not k:
            startNode = startNode.nextNode
        return startNode

    # for doubly linked lists
    # def listDelete(self, x):
    #     if x.previousNode:
    #         x.previousNode.nextNode = x.nextNode
    #     else:
    #         self.head = x.nextNode
    #     if x.nextNode:
    #         x.nextNode.previousNode = x.previousNode


    # Second method of removing an element from linked list -- traversing through the linked list class (doubly linked lists)
    # def listRemove(self, k):
    #     resultNode = self.listSearch(k)
    #     self.listDelete(resultNode)

    # a reporting method for debugging
    # def reportList(self):
    #
    #     listContents = 'Number of items: ' + str(self.counter) + '\n'
    #
    #     startNode = self.head
    #
    #     # for i in range(self.counter):
    #     #     listContents += '[[ ' +  str(startNode.data) + ' ]] => '
    #     #     startNode = startNode.nextNode
    #
    #     while startNode is not None:
    #         listContents += '[[ ' +  str(startNode.data) + ' ]] => '
    #         startNode = startNode.nextNode
    #
    #     listContents += 'None'
    #
    #     return listContents
