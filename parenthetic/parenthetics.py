from __future__ import unicode_literals
from random import choice as choice
from abc import types
import math

def generate_parenthetical_iterable(string):
    """
    Take a string and return an ordered iterable with only the "(" and ")"
    characters remaining
    """
    #  Using an abstract base class to "goose-type" check;
    #  this is an intentional part of the Python language. See README.md
    if not isinstance(string, types.StringTypes):
        raise TypeError

    set_to_find = ["(", ")"]    #Defining a filter
    characters = tuple(string)    #Turning characters into an iterable

    for character in characters:
        if character in set_to_find:
            yield character



def parenthetical(string):
    """
    Examine a string for closed, open, and well-formed parentheses;
    return a -1, 1, and 0 respectively.

    It might be helpful to recall that parenthesis is of greek etymology;
    parenthesis is singular, parentheses plural.
    """

    parentheses = generate_parenthetical_iterable(string)

    #  Score will help us keep track of parentheses state as we iterate;
    #  also will allow us to short-circuit out of for loop for open parenthesis
    score = 0

    for parenthesis in parentheses:
        if parenthesis == ")":
            score -= 1
            if score < 0:
                #  An open parenthesis exists. No need to check further.
                break
        else:
            #  Parenthesis is "(" here
            score += 1

    if score in set([1, 0, -1]):
        #  Score can be directly returned in some cases
        return score

    else:
        #  Else use copysign to transfer sign of score to 1
        return math.copysign(1, score)
