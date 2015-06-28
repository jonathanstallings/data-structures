#Parenthetics
Parenthetics includes an eponymous function which takes a string
argument and determines whether or not it has bron

##Illustrative Examples of functionality
These are all simplified examples. Any unicode characters can be
intersperced into any of the following.

###Case One: Broken Parentheses

All of the following will return -1
```
)))(((
)
()()()()()))(()))()(((()
```
###Case Two: Open Parentheses

All of the following will return 1
```
()(
()()()(
()()(((()()()
```

###Case Three: Okay Parentheses
```
All of the following will return 0
()()()()
(())
((()())()()())
```

##Helpful Resources
All of the following were helpful in constructing this code:
* [Filtering using a set constructor]
(http://stackoverflow.com/questions/3013449/list-filtering-list-comprehension-vs-lambda-filter)
* [Why isn't there a sign function in Python?]
(http://stackoverflow.com/questions/1986152/why-python-doesnt-have-a-sign-function)
* [Goose-typing is intended in Python]
(https://docs.python.org/2/glossary.html#term-abstract-base-class)

The "goose typing" coin was termed in an amusing little article by 
Alex Martelli included as part of Luciano Rahmalho's Fluent Python.
I'm tempted to do a lightining talk on it.