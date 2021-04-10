# CMPT 145 Course material
# Copyright (c) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this 
# file to a public or private website, or providing this file to a person 
# not registered in CMPT 145, constitutes Academic Misconduct, according 
# to the University of Saskatchewan Policy on Academic Misconduct.

class SuperNode(object):
    def __init__(self, value=None, next_node=None):
        self.data = value      # Private!
        self.next = next_node      # Private!

    def get_data(self):
        """
        Purpose:
            returns the data stored in the node
        Pre-conditions:
            None
        Post-condition:
            None
        Return:
            returns the data stored in the node, or None if it is empty
        """
        return self.data

    def get_next(self):
        """
        Purpose:
            returns the node stored the next field
        Pre-conditions:
            None
        Post-condition:
            None
        Return:
            returns the node stored in the next field, or None if it is empty
        """
        return self.next

    def set_data(self, value):
        """
        Purpose:
            sets the data of node to be value
        Pre-conditions:
            None
        Post-condition:
            Node now contains the data value
        Return:
            None
        """
        self.data = value

    def set_next(self, next_node):
        """
        Purpose:
            sets the next field to point to the node next_node
        Pre-conditions:
            None
        Post-condition:
            the next field now points to next_node
        Return:
            None
        """
        self.next = next_node
