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
