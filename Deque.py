#creation of Deque class
#insert an element at front of the Queue
#insert an element at rear of the Queue
#remove an element at front of the Queue
#remove an element at rear of the Queue
#get the size of the Queue

class Deque(object):

    def __init__(self):

        self.items = []

    def insertFront(self, ele):

        self.items.insert(0, ele)

    def insertRear(self, ele):

        self.items.append(ele)

    def removeFront(self):

        return self.items.pop(0)

    def removeRear(self):

        return self.items.pop()

    def size(self):

        return len(self.items)

    def isEmpty(self):

        return len(self.items) == 0

a = Deque()
