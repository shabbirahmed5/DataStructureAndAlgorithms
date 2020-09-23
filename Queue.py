#Creation of Queue class
#insert function
#delete function
#to check if the queue is empty or not
#to check the size of queue

class Queue(object):

    #initialising an array
    def __init__(self):

        self.items = []

    #function to input an element to queue on front
    def enqueue(self, ele):
        #everytime the element is inserted at first position and rest of the elements are moved aside
        self.items.insert(0, ele)

    #function to remove the last element, in this case the first element will be the last element in an array
    def dequeue(self):

        return self.items.pop()

    #function to check whether the queue is empty or not
    def isEmpty(self):
        #returns with true or false
        return len(self.items) == 0

    #function returning size of the queue
    def size(self):

        return len(self.items)


a = Queue()
a.enqueue(9)
a.enqueue(5)
a.enqueue(6)
a.enqueue(7)
a.enqueue(8)


