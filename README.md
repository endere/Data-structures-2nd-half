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

#Hash Table Functions
-_hash(self, key): Use fnv hash if function is fnv, or uses additive hash if function is add.
Time complexity: O(n)

-set(self, key, value): sends a key through a hash and then sets its value in a corresponding bucket.
Time complexity: O(n) + O(log(n)*2)

-get(self, key): Returns the value of given key from the hash table.
Time complexity O(n) + O(log(n))

#Trie Tree/Traversal 
-Functions:
-Insert: Inserts a node into the tree.
-Contains: Returns true if string is in the tree.
-Size: Return total number of words in tree.
-Remove: Remove string from tree.
-Traversal: Traverses through the tree and return a list of all strings with the given start.

#Bogo Sort:
-Randomly shuffles through until it is sorted out. 
Time Complexity Best Case = O(n)
Time Complexity Worst Case = Infinite 

#Bubble sort
-Uses the bubble sort algorithm to sort a list of numbers.
Time complexity best case: O(n)
Time complexity worst case: O(n^2)

#Insertion Sort
Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
Time Complexity Best Case = O(n)
Time Complexity Worst Case = O(n^2)

#Merge Sort 
Merge sort will divide the list of ints in half and then divide those into half and then compare each pair and swap the values where one is less than the other. Once both sides have been sorted out it will do one more sort to sort out the entire list. 
Time Complexity Best Case = O(n log n)
Time Complexity Worst Case = O(n log n)

#Quick Sort 
Quicksort is a comparison sort, meaning that it can sort items of any type for which a "less-than" relation (formally, a total order) is defined.
Time Complexity Best Case = O(n log n)
Time Complexity Worst Case = O(n^2)


#Radix Sort 
Radix sort will sort the values out by their values places starting at the end of the value. Once it has sorted through all the value places it'll sort the whole list out. 
Time Complexity Best Case = O(wn)
Time Complexity Worst Case = O(wn)

