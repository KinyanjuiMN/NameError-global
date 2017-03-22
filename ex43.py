
from sys import exit
from random import randint

"""
The game of Life begins after you are born and ends after you died
"""

def my_life():
    """ my life function """
    print "Now you find your self in the world and want to make major decisions"
    print "You have to chose between Education and No Education"
    my_choice == raw_input("> ")

    if my_choice == "education":
        return 'go_to_school'
    elif my_choice == "no education":
        return 'face_the_world'
    else:
        return 'unknow_world'

my_object=my_life()
my_object
