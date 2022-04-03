class BST:
    # Binary search tree class

    class Node:
        # Node object class

        def __init__(self, data):
            self.data = data
            self.left = None # Left child
            self.right = None # Right child

    def __init__(self):
        # create the BST and set the root
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data) # insert data at the root if there is none
        else:
            self._insert(data, self.root)  # calls _insert to recursively iterate through the list to find an insertable location

    def _insert(self, data, node):
        if data == node.data: # check for duplicates
            return

        if data < node.data:
            # left side
            if node.left is None:
                node.left = BST.Node(data) # creates the node when it has found a location
            else:
                self._insert(data, node.left) # recursive function call on the left node
        else:
            # right side
            if node.right is None:
                node.right = BST.Node(data) # creates the node when it has found a location
            else:
                self._insert(data, node.right) # recursive function call on the right node

    def __contains__(self, data):
        # checks if the data is contained in the binary search tree
        # this function supports the in keyword
        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):
        # recursive function that looks for the data in the BST
        if data == node.data: # checks if the data matches
            return True
        else:
            if data < node.data: # points to the left node
                if node.left: # if there is a left node
                   return self._contains(data, node.left)
                else:
                    return False
            else: # goes to the right node
                if node.right: # if there is a left node
                   return self._contains(data, node.right)
                else:
                    return False

    def __iter__(self):
        # this function goes through the bst to retreive all of the values from it
        # works with the in keyword in a for loop as shown below:
        # for node in bst:
        #     print(node)
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        # traverses through the BST starting from the left side, grabbing all of the smaller numbers first
        # then it goes through the right side, getting all of the larger numbers last.
        # This function is called by __iter__()
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self):
        # this function goes through the bst to retreive all of the values from it
        # works with the in keyword in a for loop as shown below:
        # for value in reversed(my_bst):
        #    print(value)   
        yield from self._traverse_backward(self.root)  # Start at the root

    def _traverse_backward(self, node):
        # traverses through the BST starting from the right side, grabbing all of the larger numbers first
        # then it goes through the left side, getting all of the smaller numbers last.
        # This function is called by __reversed__()
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)


# Example code
print("\n=========== BST CLASS EXAMPLES ===========")
tree = BST()
# inserting our nodes
tree.insert(50) # creating the root
tree.insert(25)
tree.insert(75)
tree.insert(25) # doesn't do anything because it is a duplicate
tree.insert(80)
tree.insert(60)
tree.insert(30)
tree.insert(10)
for x in tree:
    print(x) # prints each node from the tree starting from the leftmost node

print("\n=========== CONTAINS FUNCTION ===========")
print(50 in tree) # True
print(25 in tree) # True
print(81 in tree) # False
print(1 in tree) # False
print(75 in tree) # True

print("\n=========== REVERSED ITERATOR ===========")
for x in reversed(tree):
    print(x) # prints each node from the tree starting from the rightmost node