from __future__ import unicode_literals
from random import choice as choice

def generate_parenthetical_iterable(string):
    """
    Take a string and return an ordered iterable with only the "(" and ")"
    characters remaining
    """
    set_to_find = ["(", ")"]    #Defining a filter
    characters = tuple(string)    #Turning characters into an iterable

    for character in characters:
        if character in set_to_find:
            yield character



# def parenthetical(string):
#     """
#     Examine a string for closed, open, and well-formed parentheses;
#     return a -1, 1, and 0 respectively.

#     It might be helpful to recall that parenthesis is of greek etymology;
#     parenthesis is singular, parentheses plural.
#     """

#     parentheses = generate_parenthetical_iterable(string)


#     for parenthesis in parentheses:

