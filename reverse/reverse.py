class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev=None):
        """
        Method for reversing the link and then changes the pointers to the 
        reverse of the original linked list.
        """

        if node is not None:
            if node.get_next() == None:
                self.head = node
                return
            self.reverse_list(node.get_next())
            temp = node.get_next()
            temp.set_next(node)
            node.set_next(node)
        
        
        """
        These are failed attempts that I am keeping for posterity (and Future Rob fixing).
        prev = None
        current = self.head
        nex = current.get_next()
        while current:
            current.set_next(prev)
            prev = current
            current = nex
            if nex:
                nex = nex.get_next()
        self.head = prev
        """
        """
        while current:
            next = current.next_node
            current.next = prev
            prev = current
            current = next
        self.head = prev
        """


