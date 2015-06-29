from __future__ import unicode_literals

from stack import Stack


def parenthetical(string):
    """Examine string for valid use of parentheses.
    args:
        string: the unicode string to Examine
    returns:
        1 if the string is "open" -- unclosed parentheses
        0 if the string is "balanced" -- equal number of parentheses
       -1 if the string is "broken" -- closing parentheses before opening
    """
    open_parens = Stack()
    for char in string:
        if char == '(':
            open_parens.push(char)
        elif char == ')':
            try:
                open_parens.pop()
            except IndexError:
                return -1
    if len(open_parens) >= 1:
        return 1
    else:
        return 0
