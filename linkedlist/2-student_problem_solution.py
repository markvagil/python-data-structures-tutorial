class LinkedList:
    # Linked list class, which holds all of the code for the linked list, as well as the nodes that it is comprised of

    class Node:
        # Node class
        def __init__(self, amount, date, account):
            # This creates a new node object

            # For each transaction, we need to know the amount, the date, and the account that the money was sent or received by
            self.amount = amount
            self.date = date
            self.account = account
            # We need to set our pointers
            self.next = None
            self.prev = None

    def __init__(self):
        # This creates the linked list
        self.head = None
        self.tail = None

    """ 
    This function is not needed in this use case, since we don't want anyone to be able to create a new beginning for our 

    def insert_head(self, amount, date, account):
        # This function creates the head or the first element of the linked list
        # Create the new node
        new_node = LinkedList.Node(amount, date, account)  
        
        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.head will be
        # affected.
        else:
            new_node.next = self.head # Connect new node to the previous head
            self.head.prev = new_node # Connect the previous head to the new node
            self.head = new_node      # Update the head to point to the new node
    """

    def insert_tail(self, amount, date, account):
        # This function creates a new node at the end 
        
        new_node = LinkedList.Node(amount, date, account) 

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


    def __iter__(self):
        # This function iterates forwards through the linked list
        # Use this to see all transactions starting from the oldest one

        # EXAMPLE: print(list(iter(linkedlist)))

        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.amount, curr.date, curr.account  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list

    def __reversed__(self):
        # This function iterates backwards through the linked list
        # Use this to see all of the transactions starting from the most recent one

        # EXAMPLE: print(list(reversed(linkedlist)))

        curr = self.tail # start at the end
        while curr is not None:
            yield curr.amount, curr.date, curr.account
            curr = curr.prev

    def __str__(self):
        # This function allows you to print the contents of the linked list as a transaction log, starting with the most recent ones
        output = "Transaction Log: "
        balance = 0
        first = True
        for node in self:
            if first:
                first = False
            else:
                output += " --> "
            output += str(node)
            balance += node[0]
            
        output += " Current Balance: $" + str("{:.2f}".format(balance))
        return output

    def current_balance(self):
        # It's your turn now!
        # Create a function that will return the current balance,
        # and you must do it in the same manner as __str__ so that the balance is the sum of all transactions
        # we just don't want the list of transactions that is printed like in __str__, which is why we need this function

        balance = 0 # create our balance variable
        for node in self:
            # iterate through each node in the linked list, and add it's amount to the balance
            balance += node[0] # node[0] is used because each node is a tuple of information which is indexed so you can grab the first index which contains the amount
        
        return "Current Balance: $" + str("{:.2f}".format(balance)) # return our balance in the format that was requested

        """
        This is pretty simple but it shows you that linked lists are easy to use and gather data from.
        Each node is chained together so you can easily iterate through them to get the desired result that you need!

        """



# CODE BEING USED HERE

ctca = LinkedList() # ctca stands for chase total checking account
print("Mark's Chase Bank Total Checking Account")
print()
ctca.insert_tail(100, "1/5/22", "Cash Deposit")
ctca.insert_tail(-10, "1/7/22", "McDonalds")
ctca.insert_tail(50, "1/9/22", "Cash Deposit")
ctca.insert_tail(750, "1/11/22", "Check Deposit")
ctca.insert_tail(-300, "1/19/22", "Apple")
ctca.insert_tail(412.57, "1/21/22", "Check Deposit")
ctca.insert_tail(-30, "1/22/22", "Chase Bank")
ctca.insert_tail(-11.34, "1/27/22", "Taco Bell")
print(ctca) # printing the transaction log with current balance
print()

# Iterating through just the transactions themselves
print("Oldest First:")
print(list(iter(ctca)))
print()
print("Newest First:")
print(list(reversed(ctca)))



# TEST CASE FOR current_balance() function
print()
print(ctca.current_balance()) # Should output "Current Balance: $961.23"



# Created by Mark Vagil