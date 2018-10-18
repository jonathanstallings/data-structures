[![Build Status](https://travis-ci.org/jonathanstallings/data-structures.svg?branch=master)](https://travis-ci.org/jonathanstallings/data-structures)


#Data Structures
Implementation of LinkedList and Stack data structures in Python.

##LinkedList
The LinkedList class is composed of a Node base class.

Available methods inlude:
* insert(val)
* pop()
* size()
* search(val)
* remove(node)
* display()

##Stack
The Stack data class is a first-in-first-out data structure built via composition from LinkedList.
Available methods include:
* push(value)
* pop()

##Queue
The Queue data class is a first-in-last-out data structure built via encapsulation of a LinkedList.

Available methods inlude:
* enqueque(value)
* dequeque()
* len()

##Binary Heap
The Binary Heap data class is a binary tree data structure built implemented on a built-in Python
list. The binary heap default to a minheap sort, meaning that the smallest values will be sorted to
the top of the heap. Alternatively, the binary heap can be instantiated as a maxheap so that the
greatest values will be sorted to the top.

Available methods include:
* pop()
* push()
See the doc strings for implementation details.

##PriorityQ
The PriorityQ data class is a binary tree that implements sorting primarily by priority value and
secondarily by insertion order. The PriorityQ defaults to minheap sorting for both. A QNode is implemented
as a base class to containerize the value and priority and to provide convenient APIs for comparison.

Available methods include:
* insert(item)
* pop()
* peek()
See the doc strings for implementation details.

Instantiation of a PriorityQ takes an iterable which may contain (value, priority) iterables,
non-iterable values, or QNode objects.

##Graph
The graph data class is a network consisting nodes with an arbitrary number of references (edges) to other
nodes in the graph. Methods allows abilities such as adding, removing, and checking the existance of nodes
and edges in the graph. Additionaly, the graph class contains to traversal methods. Given a start node, the
methods will traverse the entire network reachable from that node and return the path travelled as a list of
nodes travelled. Both [depth-first](https://en.wikipedia.org/wiki/Graph_traversal#Depth-first_search) and [breadth first](https://en.wikipedia.org/wiki/Graph_traversal#Breadth-first_search) traversal methods are available.

Available methods include:

* nodes()
* edges()
* add_node(n)
* add_edge(n1, n2)
* del_node(n)
* del_edge(n1, n2)
* has_node(n)
* neighbors(n)
* adjacent(n1, n2)
* depth_first_traversal(start)
* breadth_first_traversal(start)
* uniform_cost_search(n1, n2)
* bellmanford(n1, n2)

The uniform_cost_search method returns a path that corresponds to the
shortest path between n1 and n2. This algorithm tracks historical paths
and is able to search for the shortest path in a relatively uncostly way.
Time complexity is O(edges + node log nodes) with relatively low memory
overhead.

The bellmanfor search method also returns the same path, but has the added
ability to handle edges with negative values and detect negative feedback
loops. It is relatively robust, but at added time complexity cost of 
O(nodes * edges).

See the doc strings for additional implementation details.

##Binary Search Tree
Contains a Node class which implements an AVL binary search tree.

Each node can be considered a binary search tree and has the usual
methods to insert, delete, and check membership of nodes. By default,
the insert and delete methods will perform self-balancing consistent
with an AVL tree. This behavior can be suppressed by passing the optional
'balanced=False' keyword argument to the insert or delete methods.

The class also supports four traversal methods which return generators:

- in_order
- pre_order
- post_order
- breadth_first.

Additionally, methods are included to help visualize the tree structure.
get_dot returns DOT source code, suitable for use with programs such as
Graphviz (http://graphviz.readthedocs.org/en/stable/index.html), and
save_render saves a rendering of the tree structure to the file system.
Passing the optional 'render=True' keyword argument to the insert and
delete methods will automatically save a render to disk upon execution.

Finally, the helper methods 'create_best_case' and 'create_worst_case'
facilitates creation of tree composeds of _n_ integers.

This module was completed with reference to the following:

[Binary Search Tree libary in Python](http://www.laurentluce.com/posts/binary-search-tree-library-in-python/)
by Laurent Luce.

[How to Balance your Binary Search Trees - AVL Trees](https://triangleinequality.wordpress.com/2014/07/15/how-to-balance-your-binary-search-trees-avl-trees/)

[The AVL Tree Rotations Tutorial](http://pages.cs.wisc.edu/~paton/readings/liblitVersion/AVL-Tree-Rotations.pdf)
by John Hargrove
Available methods include:

* insert(val, balanced=True, render=False)
* delete(val, balanced=True, render=False)
* contains(val)
* lookup(val)
* size()
* depth()
* balance()
* in_order()
* pre_order()
* post_order()
* breadth_first()
* get_dot()
* save_render()
* create_best_case()
* create_worst_case()


See the doc strings for additional implementation details.

##Hash Table
Contains a HashTable class. The [hash table](https://en.wikipedia.org/wiki/Hash_table)
is implemented on a list of lists, with a default table size of 8192. This table
size can be overridden on initialization by passing a size keyword argument. Insertion
and lookup time complexity ranges from O(1) at best to O(n) at worst.

Available methods include:

* set(key, value)
* get(key)

##Insertion Sort
This module contains the in_sort method, which performs an
in-place insertion sort on a passed in list. Insertion sort has a best case time
complexity of O(n) when list is nearly sorted, and a worst case of O(n2)
when the incoming list is already reverse sorted. While this not always
the most efficient algorithm, it is still popular when the data is nearly
sorted (because it is adaptive) or when the problem size is small.
See the excellent 'sortingalgorithms.com' for more information.

## Merge Sort
This module contains the merge_srt method, which performs an
in-place merge sort on a passed in list. Merge sort has a best case time
complexity of O(n log n) when list is nearly sorted, and also a worst case of
O(n log n). Merge sort is a very predictable and stable sort, but it is not
adaptive. See the excellent 'sortingalgorithms.com' for more information.

##Quick Sort
"""This module contains the quick sort method (quick_srt), which performs an
in-place sort on a passed in list. Quick sort has a best case time
complexity of O(n log n) when all elements are equal, and a worst case of
O(n2). Quick sort is not stable or adaptive, but it is robust and has low
overhead.

This module was completed with reference to:
[Quicksort: A Python Implementation](http://pfsensesetup.com/pythonscript.net/quicksort-a-python-implementation/)
by maximumdx

See the excellent 'sortingalgorithms.com' for more information.
