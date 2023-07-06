#!/usr/bin/python3


def canUnlockAll(boxes):
    n = len(boxes)  # Total number of boxes
    unlocked = [False] * n  # Track the unlocked status of each box
    unlocked[0] = True  # The first box is already unlocked
    stack = [0]  # Start with the first box

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
