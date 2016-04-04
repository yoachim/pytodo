import re
import os




def line2dict(inline):
    """
    Take a line of a todo.txt file and convert to a helpful dict.
    """

    result = {}
    if inline[0:2] == 'x ':
        result['done'] = True
        # see if there's a completed date
        possible_date = inline.split()[1]

    else:
        result['done'] = False

    return result


def readtodo(filename):
    """
    read in the todo.txt file
    """


# format of a pandas or numpy thing that would be handy

# line: The full text of the line
# done: bool, if is starts with "x "
# completion date: date
# creation date: date
# due date:  date object
# priority: whatever
# context(s):
# project(s):
