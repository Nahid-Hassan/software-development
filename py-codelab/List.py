"""
This python3 script file demonstrate List data structure using python3
"""


class Node:

    """
        This class has only one __init__(self, data) method that
        is simply a Node class initializer or constructor.
    """

    # function to initialize the node object
    def __init__(self, data):
        # assign data
        self.data = data
        # initialize next as null
        self.next = None


class LinkedList:

    """
        Linked List class.
        Methods:
           * __init__(self)
           * insert(data)
    """

    # function to initialize linked list object
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        pass

    def printlist(self):
        temp = self.head

        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.printlist()
