# *-* coding: utf-8 *-*
# author:Guangzhan


# Node of a Singly Linked List
class Node:
    # constructor
    def __init__(self, data):
        self.data = data
        self.next = None

    # method for setting the data field of the node
    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    # method for setting the next field of the node
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

    # method to add a node at the beginning of the list with a data
    def add_begin(self, node):
        new_node = node
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    # method to add a node after the data have the data=data. the data of the new node is value2
    def add_after(self, data, node):
        new_node = node
        current_node = self.head

        while current_node.next is not None or current_node.data != data:
            if current_node.data != data:
                new_node.next = current_node.next
                current_node.next = new_node
                self.length += 1
                return
            else:
                current_node = current_node.next

                # "The data provided is not present"

    # method to add a node at a particular position
    def add_pos(self, pos, node):
        current_node = self.head
        previous_node = self.head
        count = 0

        if pos > self.length or pos < 0:
            print("The position does not exist, please enter a valid position")
        else:
            while current_node.next is not None or count < pos:
                count += 1
                if count == pos:
                    previous_node.next = node
                    node.next = current_node
                    self.length += 1
                    return
                else:
                    previous_node = current_node
                    current_node = current_node.next

    # method to add a node at the end of a list
    def add_last(self, node):
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next
        new_node = node
        new_node.next = None
        current_node.next = new_node
        self.length += 1

    # method to delete the first node of the linked list
    def delete_big(self,):
        if self.length == 0:
            print("The list is empty")
        else:
            self.head = self.head.next
            self.length -= 1

    # method to delete the last node of the list
    def delete_last(self):
        if self.length == 0:
            print("The list is empty")
        else:
            current_node = self.head
            previous_node = self.head

            while current_node.next is not None:
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = None
            self.length -= 1

    # method to delete a node after the node having the given data
    def delete_value(self, data):
        current_node = self.head
        previous_node = self.head

        while current_node.next is not None or current_node.data != data:
            if current_node.data == data:
                previous_node.next = current_node.next
                self.length -= 1
            else:
                previous_node = current_node
                current_node = current_node.next

        print("The data provided is not present")

    # method to print the whole list
    def print_list(self):
        node_list = []
        current_node = self.head
        while current_node is not None:
            node_list.append(current_node.data)
            current_node = current_node.next
        print(node_list)


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    ll = LinkedList()
    ll.add_node(node1)
    ll.add_node(node2)
    ll.add_node(node3)
    ll.add_node(node4)
    ll.add_node(node5)
    ll.add_node(node6)
    ll.add_node(node7)
    ll.add_node(node8)
    ll.add_node(node9)
    ll.print_list()
