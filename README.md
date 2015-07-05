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

##Parenthetics
Contains the parenthetical function which checks the validity of parenthetical usage.

The function will examine a unicode string as its sole argument and return as follows:

* Return 1 if the string is "open" (there are open parens that are not closed)
* Return 0 if the string is "balanced" (there are an equal number of open and closed parentheses in the string)
* Return -1 if the string is "broken" (a closing parens has not been proceeded by one that opens)

###Examples

Open Case:
* '( ()'

Balanced Case:
* '(())'

Broken Case:
* ') ()'

###Notes
This function was written with inspiration from the work of:
* [Jason Tyler](https://github.com/jay-tyler)
* [Jim Grant](https://github.com/MigrantJ)
