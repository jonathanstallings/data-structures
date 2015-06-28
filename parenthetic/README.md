#Parenthetics
Parenthetics includes an eponymous function which takes a string
argument and determines whether or not it has bron

##Illustrative 
###Case One: Broken Parentheses

All of the following will return -1
'''
)))(((
)
()()()()()))(()))()(((()
'''
###Case Two: Open Parentheses

All of the following will return 1
'''
()(
()()()(
()()(((()()()
'''

###Case Three: Okay Parentheses
'''
All of the following will return 0
()()()()
(())
((()())()()())
'''