#!/usr/bin/python3


def listUnlockCheck(boxes):
    if isinstance(boxes, list):
        for box in boxes:
            if isinstance(box, list):
                for value in box:
                    if isinstance(value, int):
                        return True
                    return False
    return False


def canUnlockAll(boxes: list) -> bool:
    """a function that unlock boxes.
    Arg: Array of arrays
    returns: boolean"""
    if listUnlockCheck(boxes):
        # Empty array
        openbox = [boxes[0]]

        # Iterate through the open Box
        for box in openbox:
            for key in box:
                if len(boxes) - 1 >= key >= 1 and isinstance(key, int):
                    if boxes[key] not in openbox:
                        openbox.append(boxes[key])
        if len(openbox) == len(boxes):
            return True
    return False

