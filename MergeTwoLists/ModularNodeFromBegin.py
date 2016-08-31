# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2016-8-29 21:09:46
#
# Book Title			: Data Structures And Algorithms Made In Python


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next


class LinkList(object):
    def __init__(self):
        self.head = None

    def modular_node_from_begin(self, k):
        current_node = self.head
        modular_node = None
        i = 1
        if k <= 0:
            return None
        while current_node is not None:
            if i % k == 0:
                modular_node = current_node
            i += 1
            current_node = current_node.get_next()
        print(modular_node.get_data())

    def insert_at_end(self, item):
        current_node = self.head
        if current_node is None:
            node = Node(item)
            node.set_next(None)
            self.head = node
            return
        while current_node.get_next() is not None:
            current_node = current_node.get_next()
        node = Node(item)
        current_node.set_next(node)


if __name__ == '__main__':
    ls = LinkList()
    ls.insert_at_end(1)
    ls.insert_at_end(2)
    ls.insert_at_end(3)
    ls.insert_at_end(4)
    ls.modular_node_from_begin(3)
