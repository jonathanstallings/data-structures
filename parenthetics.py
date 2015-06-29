from __future__ import unicode_literals

from stack import Stack


def parenthetical(string):
    """Examine string for valid use of paretheses.
    args:
        string: the unicode string to Examine
    returns:
        1 if the string is "open"
        0 if the string is "balanced"
       -1 if the string is "broken"
    """
    open_parens = Stack()
    for char in unicode(string):
        if char == '(':
            open_parens.push(char)
        elif char == ')':
            try:
                open_parens.pop()
            except IndexError:
                return -1
    if len(open_parens) > 1:
        return 1
    else:
        return len(open_parens)
