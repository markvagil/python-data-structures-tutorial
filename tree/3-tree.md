# Tree

A tree is a datastructure where there is a root node which has child nodes. The node above the current node is referred to as the parent node. So the structure consists of a root, children nodes, and parents depending on which node you are focusing on. For example, our tree will be this:
```
    2 - root and parent
   / \ 
  1   3 - children
```
The height of this tree would be 2, counting the root plus one set of children.

There are 4 main types of trees:

### General tree

A general tree data structure has no restriction on the number of nodes. It means that a parent node can have any number of child nodes.  

### Binary tree

A node of a binary tree can have maximum number of two child nodes. In the given tree diagram, node B, D, and F are left children, while E, C, and G are the right children.  

### Balanced tree

If the height of the left sub-tree and the right sub-tree are equal or differs at most by 1, the tree is known as balanced tree data structure.  

### Binary search tree

As the name implies, binary search trees are used for various searching and sorting algorithms. The examples include AVL tree and red-black tree. It is a non-linear data structure. It shows that the value of the left node is less than its parent, while the value of right node is greater than its parent.  

For more information about trees and what they can be used for, visit [this page](https://www.geeksforgeeks.org/introduction-to-tree-data-structure/).

## Example Problem

For our example, I will show a basic binary search tree which is used to store numbers and presort them. Our root node will be 50. Every number less than 50 will be sorted into the left node, and every number greater than 50 will be sorted into the right node. This is what it will look like:
```
        50
       /  \
     25    75
    / \    / \
  10  30  60  80 
```
[Click to view example code](3-tree.py)

## Student Problem

We want to expand on this example code. We need to be able to get the height of the tallest sub tree in our binary search tree. You will need to create a recursive method to find the height of each subtree of each node until there isn't another child node, and return it. You will be writing your code in the _get_height(self, node) function. The tests for the function have already been written for you at the bottom of the file. If your code is written correctly, then it will output what the comments say it should.

[Click to view problem](3-student_problem.py)

Here is the [solution](3-student_problem_solution.py) if you are unable to complete the problem.

