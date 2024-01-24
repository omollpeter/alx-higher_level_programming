#!/usr/bin/python3
"""Contains class defintion for a node and a singly linked list"""


class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes instance attributes for a Node instance

        Args:
            data: Node data(int)
            next_node: Pointer to the next node
        """

        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        # if next_node is not None or not isinstance(next_node, Node):
        #     raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Returns the value of data"""
        return self.__data

    @data.setter
    def data(self, data):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """Retrieves the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None:
            self.__next_node = None
        else:
            if not isinstance(value, Node):
                raise TypeError("next_node must be a Node object")
            self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initilizes instance attributes"""
        self.__head = None

    def __repr__(self):
        """Prints the singly linked list"""
        temp = self.__head
        msg = ''
        while temp.next_node:
            msg += str(temp.data) + '\n'
            temp = temp.next_node
        msg += str(temp.data)
        return msg

    def insert_end(self, value):
        """Inserts a new node at the end of a singly linked list

        Args:
            value: Value to be inserted
        """
        if self.__head is None:
            self.__head = Node(value)
            return
        temp = self.__head
        while temp.next_node:
            temp = temp.next_node
        temp.next_node = Node(value)

    def insert_beginning(self, value):
        """Inserts a new node at the end of a singly linked list

        Args:
            value: Value to be inserted
        """
        new = Node(value, self.__head)
        self.__head = new

    def sorted_insert(self, value):
        """Inserts a new node into the correct sorted position
        of the linked list

        Args:
            value: Value to be inserted
        """
        if self.__head is None or self.__head.data == value:
            self.insert_beginning(value)
            return
        temp = self.__head
        prev = None
        if temp.data > value:
            self.insert_beginning(value)
            return
        new = Node(value)
        while temp.next_node:
            if temp.data >= value:
                if prev is not None:
                    prev.next_node = new
                new.next_node = temp
                return
            prev = temp
            temp = temp.next_node
        temp.next_node = new

    def print_ll(self):
        temp = self.__head
        while temp:
            print(temp.data)
            temp = temp.next_node
