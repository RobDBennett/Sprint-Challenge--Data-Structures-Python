class RingBuffer:
    def __init__(self, capacity):
        """"
        Requires capacity to be an integer.
        """
        self.capacity = capacity
        self.data = []
        self.current = None

    def append(self, item):
        """
        Method that compares the current data in the list to it's capacity. While the list is not
        at capacity, it adds to the end. Once it is full, it impliments a logic shift to replace
        the oldest value on the list.
        """
        if len(self.data) < self.capacity:
            self.data.append(item)
        elif len(self.data) == self.capacity and self.current == None:
            self.current = 0
            self.data[self.current] = item
            self.current = (self.current + 1)%self.capacity
        elif len(self.data) == self.capacity and self.current != None:
            self.data[self.current] = item
            self.current = (self.current +1) % self.capacity


    def get(self):
        """Returns the value of the list."""
        return self.data

