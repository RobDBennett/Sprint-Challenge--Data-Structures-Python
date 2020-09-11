"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        """
        Instantiates a class with a value and nodes to the left and right.
        """
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        """
        Checks if the value inputted is less than or greater than the base value.
        It then repeats this process until there is a None value, and adds the node there.
        """
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        """
        Checks to see if a given value is within the tree already.
        """
        if self.value == target:
            return True
        elif target < self.value and self.left:
            return self.left.contains(target)
        elif target >= self.value and self.right:
            return self.right.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        """
        Returns the highest value in the tree. 
        Given that this should be the most extreme right value, thats all it checks for.
        Utilizes recursion.
        """
        if not self:
            return None
        return self.right.get_max() if self.right else self.value #Ternarary Operator

    def get_min(self):
        """
        Returns the lowest value in the tree.
        Given that this should be the most extreme left value, thats all it checks for.
        Utilizes recusion.
        """
        if not self:
            return None
        return self.left.get_min() if self.left else self.value #Ternarary Operator

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        """
        Performs the function fn() on each value of the node using recursion.
        """
        if self.value:
            fn(self.value)
            if self.left:
                self.left.for_each(fn)
            if self.right:
                self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        """
        This prints the order of the node values from low to high.
        Given that the lowest value should be the most extreme left, 
        and the highest the most extreme right, that is all the checks before printing.
        """
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        """
        This generates a list, starting with the given node. It then goes through the nodes, 
        removing a value and adding it to the list.
        This utilizes a queue (that is to say, remove the first thing on the list.)
        """
        queue = []
        queue.append(self)
        while len(queue):
            current = queue.pop(0)
            print(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        """
        Gives the value of each node, starting with a given node. Then it repeats the process for the left and then the right.
        This utilizes a stack (that is to say, removes the last thing on the list)
        """
        #print(self.value)
        #if self.left:
        #    self.left.dft_print()
        #if self.right:
        #    self.right.dft_print()
        stack = []
        stack.append(self)
        while len(stack):
            current = stack.pop()
            print(current.value)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        """
        This gives the pre-order for the depth first transverse.
        """
        print(self.value)
        if self.left:
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()

    def in_order_dft(self):
        """
        This gives the in-order for the depth first transverse.
        """
        if self.left:
            self.left.in_order_dft()
        print(self.value)
        if self.right:
            self.right.in_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        """
        This gives the post order for the depth first transverse.
        """
        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()  
