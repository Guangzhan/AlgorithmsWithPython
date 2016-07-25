# *-* coding:utf-8 *-*


# node primary
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

    @property
    def has_next(self):
        return self.next is not None


class LinkedList(object):
    def __init__(self):
        self.length = 0
        self.head = None

    def add_node(self, node):
        if 0 == self.length:
            self.add_beg(node)
        else:
            self.add_last(node)

    # method to add a node at the begin of list
    def add_beg(self, node):
        new_node = node
        new_node.next = self.head
        self.head = node
        self.length += 1

    # method to add a node after the node having the data=data. The data of the new node is value2
    def add_after(self, data, node):
        new_node = node
        current_node = self.head

        while current_node.next is not None or current_node.data != data:
            if current_node.data == data:
                new_node.next = current_node.next
                current_node.next = new_node
                self.length += 1
                return
            else:
                current_node = current_node.next
        print("The data provided is not present")

    # method to and a node at the pos of the list
    def add_pos(self, pos, node):
        count = 0
        current_node = self.head
        previous_node = self.head

        if pos > self.length or pos < 0:
            print("The position does not exist. Please enter a valid position")
        else:
            while current_node.next is not Node or count < pos:
                count += 1
                if count == pos:
                    previous_node.next = node
                    node.next = current_node
                    self.length += 1
                    return
                else:
                    previous_node = current_node
                    current_node = current_node.next

    # method to add a not at the end of the list
    def add_last(self, node):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        new_node = node
        new_node.next = None
        current_node.next = new_node
        self.length += 1

    # method to print the whole list
    def print_list(self):
        node_list = []
        current_node = self.head
        while current_node is not None:
            node_list.append(current_node.data)
            current_node = current_node.next
        print(node_list)

    # method to delete the first node of linked list
    def delete_beg(self):
        if self.length == 0:
            print("The list is empty")
        else:
            self.head = self.head.next
            self.length -= 1

    # method to delete the last node of linked list
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
    def delete(self, data):
        current_node = self.head
        previous_node = self.head

        while current_node.next is not None or current_node.data != data:
            if current_node.data == data:
                previous_node.next = current_node.next
                self.length -= 1
                return
            else:
                previous_node = current_node
                current_node = current_node.next
            print("The data provided is not present")


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)

    ll = LinkedList()
    ll.add_node(node1)
    ll.add_node(node2)
    ll.add_node(node3)
    ll.add_node(node4)
    ll.add_node(node5)
    ll.add_last(node6)
    print(ll.length)
    ll.add_beg(node7)
    ll.add_last(node8)
    ll.delete_beg()
    ll.delete_last()

    ll.print_list()































