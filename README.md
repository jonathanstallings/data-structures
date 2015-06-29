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

See the doc strings for implementation details.

##Stack
The Stack data class is a first-in-first-out data structure built via composition from LinkedList.
Available methods include:
* push(value)
* pop()

See the doc strings for implementation details.

##Parenthetics
Contains the parenthetical function which checks the validity of parenthical usage.

The function will examine a unicode string as its sole argument and return as follows:

* Return 1 if the string is "open" (there are open parens that are not closed)
* Return 0 if the string is "balanced" (there are an equal number of open and closed parentheses in the string)
* Return -1 if the string is "broken" (a closing parens has not been proceeded by one that opens)

###Exammples

Open Case:
* '( ()'

Balanced Case:
* '(())'

Broken Case:
* ') ()'

###Notes
This function was written with inspiration from the work of:
* [Jason Tyler](https://github.com/jay-tyler)
*[Jim Grant](https://github.com/MigrantJ)
