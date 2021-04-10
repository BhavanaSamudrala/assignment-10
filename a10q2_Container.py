
from Node import Node


class Container(object):


    def __init__(self):
        self.__bottom = None
        self.__top = None
        self.__size = 0

    def size(self):
        """
        Purpose
            returns the number of data values in the stack
        Return:
            The number of data values in the stack
        """
        return self.__size

    def is_empty(self):
        """
        Purpose
            checks if the stack has no data in it
        Return:
            True if the stack has no data, or false otherwise
        """
        return self.__size == 0

    def add_top(self, value):
        self.__top = Node(value, self.__top)

        if self.__bottom is None:
            self.__bottom = self.__top

        self.__size += 1

    def add_bottom(self, value):
        new_node = Node(value)

        if self.__size == 0:
            self.__top = new_node
        else:
            self.__bottom.set_next(new_node)

        self.__bottom = new_node
        self.__size += 1

    def pop_top(self):

        result = self.__top
        self.__top = self.__top.get_next()

        # check if it was last node.
        if self.__top is None:
            self.__bottom = None

        self.__size -= 1
        return result.get_data()

    def pop_bottom(self):

        if self.__size == 1:
            return self.pop_top()

        prev = self.__top
        current = prev.get_next()

        while current.get_next() is not None:
            prev = current
            current = current.get_next()

        prev.set_next(None)
        self.__bottom = prev
        self.__size -= 1
        return current.get_data()

    def peek(self):
        return self.__top.get_data()

    def to_string(self):
        if self.is_empty():
            result = 'EMPTY'
        else:
            walker = self.__top

            value = walker.get_data()
            result = str(value) + ' |'

            while walker.get_next() is not None:
                walker = walker.get_next()

                value = walker.get_data()
                result += ' *-]-->[ ' + str(value) + ' |'

        return result
