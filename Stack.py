#Creating Stack class
#creating of push function
#creating of pop function
#creating of isEmpty function
#creating of peek function

class Stack(object):

    def __init__(self):

        self.items = []

    def push(self, ele):

        self.items.append(ele)

    def isEmpty(self):

        return len(self.items) == 0

    def pop(self):

        return self.items.pop()

    def peek(self):

        return self.items[len(self.items)-1]

a = Stack()
a.push(3)
a.push(4)

print(a.pop())
print(a.peek())
print(a.pop())
print(a.isEmpty())
