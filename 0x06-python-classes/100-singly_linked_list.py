#!/usr/bin/python3
"""Define Class Node"""


class Node:
    """Creates a linked list

    Args:
        data (int): input data.
        next_node (Node): points to the next node.
    """
    def __init__(self, data, next_node=None) -> None:
        """Initialization method

        Attributes:
            data (int): input data.
            next_node (Node): points to the next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Data getter

        Returns:
            data (int): input data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Data setter

        Args:
            value (int): input integer.
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value
        return None

    @property
    def next_node(self):
        """Node getter

        Returns:
            next_node (Node): pointer to next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Node setter

        Args:
            value (Node): poinetr to next node.
        """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
        return None


"""Define Class SinglyLinkedList"""


class SinglyLinkedList:
    """Sorts linked list (ASC) and prints it"""
    def __init__(self):
        """Initialization method

        Args:
            head (Node): head pointer to node.
        """
        self.__head = None

    def __str__(self) -> str:
        """Returns string representation of Node object

        Returns:
            string (str): output string for Node object.
        """
        temp = self.__head
        """Empty string"""
        string = ""
        while (temp is not None):
            string = string + str(temp.data)
            temp = temp.next_node
            if (temp is not None):
                string = string + "\n"
        return string

    def sorted_insert(self, value):
        """Sorts Node linked list in ascending order"""
        if type(value) is not int:
            raise TypeError("value must be an integer")
        store = Node(value)
        """Assign store to head if is None"""
        if self.__head is None:
            self.__head = store
            return
        """Hold address of head"""
        temp = self.__head
        if store.data < temp.data:
            store.next_node = self.__head
            self.__head = store
            return
        """Loop through so long you have not reached None in temp"""
        while temp.next_node is not None and store.data > temp.next_node.data:
            temp = temp.next_node
        store.next_node = temp.next_node
        temp.next_node = store
        return
