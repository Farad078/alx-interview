#!/usr/bin/python3


def canUnlockAll(boxes: list) -> bool:
    """a function that unlock boxes.
    Arg: Array of arrays
    returns: boolean"""

    # Empty array
    openbox = [boxes[0]]

    # Iterate through the open Box
    for box in openbox:
        if len(box) > 0:
            for key in box:
                if isinstance(key, int):
                    if len(boxes) - 1 >= key >= 1:
                        if boxes[key] not in openbox:
                            openbox.append(boxes[key])
                else:
                    return False
    if len(openbox) == len(boxes):
        return True
    return False

