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
    def next_node(self, next_node):
        if next_node is not None or not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initilizes instance attributes"""
        self.__head = None

    def __repr__(self):
        """Prints the singly linked list"""
        temp = self.__head
        while temp:
            print(temp.data)
            temp = temp.next_node
        return ''

    def sorted_insert(self, value):
        """Inserts a new node into the correct sorted position

        Args:
            value: Value to be inserted
        """
        new = Node(value)
        if self.__head == None:
            self.__head = new
        else:
            temp = self.__head
            while temp.next_node:
                if temp.data > value:
                    prev = temp
                    new.next_node = temp
                temp = temp.next_node

sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)