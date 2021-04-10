import SuperNode as N


class LocationNode(N.SuperNode):

    def __init__(self, value=None, next_node=None):
        """
        Purpose: creates an LocationNode without data
        Pre-condition: None
        Post-condition: An empty Location is created
        Return: None
        """
        # call SuperNode's constructor to create the node with given values
        super().__init__(value, next_node)

    def get_current_location(self):
        """
        Purpose:
            returns the current location stored in the node
        Pre-condition:
            None
        Pre-condition:
            None
        Return:
            returns current location stored in the node, or None if it is empty
        """
        # return the data stored in the node
        return self.get_data()

    def get_next_location(self):
        """
        Purpose:
            returns the next location node
        Pre-conditions:
            None
        Post-condition:
            None
        Return:
            returns the next location node , or None if it is empty
        """
        # return the next node
        return self.get_next()

    def set_current_location(self, value):
        """
        Purpose:
            sets the value of the current location node
        Pre-conditions:
            None
        Post-condition:
            Current location node now contains the data value
        Return:
            None
        """
        # sets the data of the node to value using the SuperNode's method
        self.set_data(value)

    def set_next_location(self, next_location):
        """
        Purpose:
            sets the next location node
        Pre-conditions:
            None
        Post-condition:
            the next field now points to next location node, i.e., next_location
        Return:
            None
        """
        # sets the next node of the node to next_location using SuperNode's method
        self.set_next(next_location)

    def to_string(self):
        """
        Purpose: Create a string representation of the container. E.g.,
        [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
        where 1 is the head of the container and 3 is the end of the container
        Pre-conditions: None
        Post_conditions: None
        Return: A string representation of the container.
        """

        # special case: empty stack
        if self.get_data == None:
            result = 'EMPTY'
        else:
            walker = self
            value = walker.get_current_location()

            result = '[ ' + str(value) + ' |'
            while walker.get_next_location() is not None:
                walker = walker.get_next_location()
                value = walker.get_current_location()

                result += ' *-]-->[ ' + str(value) + ' |'

            result += ' / ]'

        return result

