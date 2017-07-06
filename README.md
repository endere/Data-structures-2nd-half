# Data-structures
Binary Search Tree: 

#Authors:
-Erik Enderlein
-Anna Shelby 

#Author Emails:
-bonanashelby@gmail.com
-erik.end@gmail.com

#Binary Search Tree Functions
-insert(self, val): will insert the value val into the BST. If val is already present, it will be ignored.

-search(self, val): will return the node containing that value, else None.

-size(self): will return the integer size of the BST (equal to the total number of values stored in the tree). It will return 0 if the tree is empty.

-depth(self): will return an integer representing the total number of levels in the tree. If there are no values, depth is 0, if one value the depth should be 1, if two values it will be 2, if three values it may be 2 or 3, depending, etc.

-contains(self, val): will return True if val is in the BST, False if not.

-balance(self): will return an integer, positive or negative that represents how well balanced the tree is. Trees which are higher on the left than the right should return a positive value, trees which are higher on the right than the left should return a negative value. An ideally-balanced tree should return 0.

-breadth_first(self): Generator function that yields values from the tree in a breadth first order.

-pre_order(self): Generator function that yields values from the tree in pre order.

-post_order(self): Generator function that yields values from the tree in post order.

-in_order(self): Generator function that yields values from the tree in numerical order.

-deletion(self): Deletes a node from the tree, while keeping the shape and order of the tree intact.
