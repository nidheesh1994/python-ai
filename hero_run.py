import hero_token
from depth_first_search import *
from breadth_first_search import *
import time
import sys
sys.setrecursionlimit(100000)
import faulthandler


faulthandler.enable()

def display_paths(paths):
    for path in paths:
        persons, boat = path

        left = [person for person in persons if persons[person] == 'left']
        right = [person for person in persons if persons[person] == 'right']

        state = ""
        for person in left:
            state += person[0]+str(person[1]) + " "
    
        if boat == 'left':
            state += " |_____________ "
        else:
            state += " _____________| "


        for person in right:
            state += person[0]+str(person[1]) + " "
    
        print(state)
        print()
        time.sleep(1)


h = hero_token.Hero_Token()

print(h.start())
# paths = depth_first_search(h, h.start())

paths = breadth_first_search(h, [[h.start()]])

display_paths(paths)
