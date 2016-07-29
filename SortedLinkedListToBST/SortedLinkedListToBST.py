# *-* coding: utf-8 *-*
# author:Guangzhan


# Node of a Singly Linked List
class Node:
    # constructor
    def __init__(self, data):
        self.data = data
        self.next = None

    # method for setting the data filed of the node
    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    @property
    def has_next(self):
        return self.next is None


# class for defining a linked list
class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    # method to add a node in the linked list
    def add_node(self, node):
        if self.length == 0:
            self.add_begin(node)
        else:
            self.add_last(node)
