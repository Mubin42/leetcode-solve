# define single node for the linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.head = None


class LinkedList:
    def __init__(self, value=0, head=None):
        self.head = head

    # now we can start add functionality
    def append(self, new_node):
        pass