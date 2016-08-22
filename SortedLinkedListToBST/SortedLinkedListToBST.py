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

    # method to delete a node at a particular position
    def delete_pos(self, pos):
        count = 0
        current_node = self.head
        previous_node = self.head

        if pos > self.head or pos < 0:
            print("The position does not exist.")
        else:
            while current_node.next is not None or count < pos:
                count += 1
                if count == pos:
                    previous_node.next = current_node.next
                    self.length -= 1
                    return
                else:
                    previous_node = current_node
                    current_node = current_node.next

    # return the length of the list
    def get_length(self):
        return self.length

    # return the first element of the list
    def get_first(self):
        if self.length == 0:
            print("The list is empty")
        else:
            return self.head.data

    # return the last element of the list
    def get_last(self):
        if self.length == 0:
            print("The list is empty")
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            return current_node.data

    # method to get a node at any position
    def get_pos(self, pos):
        count = 0
        current_node = self.head

        if pos > self.length or pos < 0:
            print("The position does not exist")
        else:
            while current_node.next is not None or count < pos:
                count += 1
                if count == pos:
                    return current_node.data
                else:
                    current_node = current_node.next

    # method to print the whole list
    def print_list(self):
        node_list = []
        current_node = self.head
        while current_node is not None:
            node_list.append(current_node.data)
            current_node = current_node.next
        print(node_list)


class BSTNode:
    def __init__(root, data=None):
        root.left = None
        root.right = None
        root.data = data


def insert_node(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                insert_node(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert_node(root.right, node)


def delete_node(root, data):
    if root.right == data:
        if root.right and root.left:
            [psucc, succ] = find_min(root.right, root)

            if psucc.left == succ:
                psucc.left = succ.right
            else:
                psucc.right = succ.right
            succ.left = root.left
            succ.right = root.right
            return succ
        else:
            if root.left:
                return root.left
            else:
                return root.right
    else:
        if root.data > data:
            if root.left:
                root.left = delete_node(root.left, data)
            else:
                if root.right:
                    root.right = delete_node(root.right, data)
    return root


def find_min(root, parent):
    if root.left:
        return find_min(root.left)
    else:
        return [parent, root]


# method to Traversal tree preOrder
def preorder_traversal(root):
    if not root:
        return
    print(root.data)
    preorder_traversal(root.left)
    preorder_traversal(root.right)


def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    print(root.data)
    inorder_traversal(root.right)


def sorted_list_to_bst(ll, start, end):
    if start > end:
        return None
    mid = start + (end - start) / 2
    left = sorted_list_to_bst(ll, start, mid - 1)
    root = BSTNode(ll.head.data)
    ll.delete_big()
    root.left = left
    root.right = sorted_list_to_bst(ll, mid + 1, end)
    return root


def convertSortedListToBST(ll, n):
    return sorted_list_to_bst(ll, 0, n - 1)


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
    root = convertSortedListToBST(ll, ll.length)
    inorder_traversal(root)

