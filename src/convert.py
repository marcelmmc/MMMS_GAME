import itertools

def is_pressed(keypress):
    return keypress[1]

def same_key(k1, k2):
    return k1[2] == k2[2]

def process_keypresses(l):
    result = []

    l = list(itertools.dropwhile(lambda x: not is_pressed(x), l))

    currently_pressed = set()
    to_be_released = set()

    for keypress in l:
        if is_pressed(keypress):
            currently_pressed.add(keypress)
            to_be_released.add(keypress)
        else: # key was released
            matching_element = set(filter(lambda x: same_key(keypress, x), to_be_released))
            to_be_released = to_be_released - matching_element

        if len(to_be_released) == 0:
            result.append(list(currently_pressed))
            currently_pressed = set()

    return result

# remove duplicates in currently_pressed

'''
def convert_to_concurrent_presses(l):
    for keypress in l:
        if keypress.pressed:
            currently_pressed.append(keypress)
            to_be_released.append(keypress)
        else: # key was released
            to_be_released.remove(keypress)
        
        if len(to_be_released) == 0:
            result.append(currently_pressed)

'''
