# *-* coding :utf-8 *-*
"""
    author: Guangzhan
    create: 2016/9/6 20:01
"""

class Node:
    # Constructor to initialize data
    # If data is not given by user, its taken as None
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def setPrev(self, prev):
        self.prev = prev

    def getPrev(self):
        return self.prev

    def hasPrev(self):
        return self.prev is not None

    def __str__(self):
        return "Node[Data = %s]" % (self.data,)


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(data, None, current)
            self.tail = current.next

    def fwd_print(self):
        current = self.head
        if current is None:
            print("No elements")
            return False
        while current is not None:
            print(current.data)
            current = current.next
        return True

if __name__ == '__main__':
    ll = DoubleLinkedList()

    # Inserting Values
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)

    # Forward Print
    ll.fwd_print()












