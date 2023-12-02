import itertools

def is_pressed(keypress):
    return keypress[1]

def same_key(k1, k2):
    return k1[2] == k2[2]

def match_one_key(keypress, keyboard_type):
    timestamp = keypress[0]
    keycode = keypress[2]

    # lowercase letters
    if keycode >= 0x41 and keycode <= 0x5A:
        return (timestamp, chr(keycode).lower(), keyboard_type)
    
    # digits
    if keycode >= 0x30 and keycode <= 0x39:
        return (timestamp, chr(keycode), keyboard_type)
    
    # punctuation
    if keycode == 190:
        return (timestamp, '.', keyboard_type)
    if keycode == 188:
        return (timestamp, ',', keyboard_type)
    if keycode == 189:
        return (timestamp, '-', keyboard_type)
    
    # backspace
    if keycode == 0x08:
        return (timestamp, '', keyboard_type)
    
    # space
    if keycode == 0x20:
        return (timestamp, ' ', keyboard_type)
    
    
    return None

def match_two_keys(k1, k2, keyboard_type):
    # sort keypresses
    if k1[2] > k2[2]:
        k1, k2 = k2, k1
    
    # get average of timestamps
    avg = (k1[0] + k2[0]) / 2
    
    # uppercase letters
    if k1[2] == 0x10 and (k2[2] >= 0x41 and k2[2] <= 0x5A):
        return (avg, chr(k2[2]), keyboard_type)
    
    # punctuation
    if k1[2] == 0x10 and k2[2] == 190:
        return (avg, ":", keyboard_type)
    if k1[2] == 0x10 and k2[2] == 188:
        return (avg, ";", keyboard_type)
    if k1[2] == 0x10 and k2[2] == 189:
        return (avg, "_", keyboard_type)

    return None

def convert_to_one_key(l, keyboard_type):
    if len(l) > 2:
        return None # we're not processing those kinds of combinations
    if len(l) == 1:
        return match_one_key(l[0], keyboard_type)
    if len(l) == 2:
        return match_two_keys(l[0], l[1], keyboard_type)
        

def process_keypresses(l, keyboard_type):
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
            result.append(convert_to_one_key(list(currently_pressed), keyboard_type))
            currently_pressed = set()

    return result
