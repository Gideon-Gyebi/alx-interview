#!/usr/bin/python3
'''Minimum Operations Interview'''


def minOperations(n):
    '''calculating the fewest number of
    operations needed to result in exactly n H
    characters in this file.
    Returns:
        Integer : if n is impossible to achieve, return 0
    '''
    pasted_chars = 1  # how many chars are in the file
    clipboard = 0  # how many H's were copied
    counter = 0  # operations counter

    while pasted_chars < n:
        # if didn't copy anything yet
        if clipboard == 0:
            # copy all
            clipboard = pasted_chars
            # incrementing operations counter
            counter += 1

        # if have not pasted anything yet
        if pasted_chars == 1:
            # paste
            pasted_chars += clipboard
            # incrementing operations counter
            counter += 1
            # continuing to next loop
            continue

        remaining = n - pasted_chars  # remaining chars to Paste
        if remaining < clipboard:
            return 0

        # if cannot be devided
        if remaining % pasted_chars != 0:
            # paste current clipboard
            pasted_chars += clipboard
            # incrementing operations counter
            counter += 1
        else:
            # copy all
            clipboard = pasted_chars
            # paste
            pasted_chars += clipboard
            # incrementing operations counter
            counter += 2

    # if the desired result is acchieved
    if pasted_chars == n:
        return counter
    else:
        return 0
