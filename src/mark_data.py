import itertools

CHARACTERS_PER_WORD = 5

# typing speed (words per minute)
def wpm(keypresses, duration):
    return (len(keypresses) / (CHARACTERS_PER_WORD * duration / 60))

# accuracy (amount of keys backspaced)
def accuracy(keypresses):
    backspaces = len(list(filter(lambda x: x[1] == '', keypresses)))
    return (1 - backspaces / len(keypresses))

# errors
def mistyped_keys(keypresses):
    result = []

    i = 0
    while i != len(keypresses) - 1:
        if keypresses[i][1] == '':
            backspaces = list(itertools.takewhile(lambda x: x[1] == '', keypresses[i:]))
            mistyped = list(map(lambda x: x[1], keypresses[i - len(backspaces) : i]))
            result.append(mistyped)
            i += len(backspaces)
            continue

        i += 1

    # flatten the list, remove the duplicates
    result = list(itertools.chain.from_iterable(result))
    return set(result)

# typing frequency per side
# at what speed do you type with either hand
def frequency_per_side():
    pass