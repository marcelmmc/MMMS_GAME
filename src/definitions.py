from enum import Enum

class Side(Enum):
    LEFT = 0
    RIGHT = 1
    LEFT_RIGHT = 2
    RIGHT_LEFT = 3
    ERROR = 4

#Create list of keyboards by mechanical, semimechaniacal, small, and other
keyboards = ['Mechanical', 'Semimechanical', 'Membrane', 'Other']

#Key distance from before and after
rights_key = ['q','w','e','r','t','g','f','d','s','a','z','x','x','c','b','\`']
lefts_key = ['y','u','i','o','p','h','j','k','l','n','m','v','[',']',';','\'',',','.','/']

