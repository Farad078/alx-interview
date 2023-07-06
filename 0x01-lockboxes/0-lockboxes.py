#!/usr/bin/python3


def canUnlockAll(boxes: list) -> bool:
    """a function that unlock boxes.
    Arg: Array of arrays
    returns: boolean"""

    # Empty array
    openbox = [boxes[0]]

    # Iterate through the open Box
    for box in openbox:
        for key in box:
            if len(boxes) - 1 >= key >= 1:
                if boxes[key] not in openbox:
                    openbox.append(boxes[key])
    if len(openbox) == len(boxes):
        return True
    return False
