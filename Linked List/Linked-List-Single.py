class Node:
  def __init__(self, data):
    self.head = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

ls = LinkedList()
ls.head = Node(1)
ls.