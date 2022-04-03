# Linked List

Linked Lists are a an advancement of a typical stack. Linked lists are different from regular lists where each item or "node" points to the next one in the list. Each linked list contains a head node which is the beginning, nodes in between, and a tail node at the end. There are 3 main types of linked lists, singly, doubly, and circular linked lists. A singly linked list consists of nodes that only point to the next node (one direction). A doubly linked list has nodes that point to the next node and the previous node as well (both directions). A circular linked list has nodes that point all the way around, so the tail will actually point to the head and vice versa. A linked list can also be thought of as a chain, when a single link is broken the chain doesn't work anymore.

For more information about linked lists, visit [this page](https://www.tutorialspoint.com/data_structures_algorithms/linked_list_algorithms.htm#:~:text=A%20linked%20list%20is%20a,used%20data%20structure%20after%20array.).

## Example Problem

For our example, we will use a linked list to record bank account deposits and withdrawals. The linked list data structure is essential in this scenario because it functions as a failsafe against someone tampering with the bank account records. If someone decides to hide or remove a transaction from the history, the chain is broken and you know fraud has occurred. It also serves as a detailed event based record, each node contains each withdrawal or deposit event. Another security measure this has is that the account balance is the sum of all transactions, that way nobody can just change the balance for any reason. The head contains the initial balance at the time of account opening. The tail contains the most recent transaction.

[Click to view example code](2-linked_list.py)

## Student Problem

Now it's your turn to solve a problem using linked lists. This problem extends from our example, because we need to add an important feature to it. We need to be able to get the current balance without printing the entire transaction log (each node in the linked list). Try it for yourself, it's not too difficult!

[Click to view problem](2-student_problem.py)

Here is the [solution](2-student_problem_solution.py) if you are unable to complete the problem.

