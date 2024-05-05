#!/usr/bin/python3
"""0-lockboxes.py"""


def canUnlockAll(boxes):
    """Set to keep track of unlocked boxes"""
    unlocked = {0}
    keys_to_check = boxes[0]
    while keys_to_check:
        key = keys_to_check.pop()
        if key < len(boxes) and key not in unlocked:
            unlocked.add(key)
            keys_to_check.extend(boxes[key])
    if len(unlocked) == len(boxes):
        return True
    else:
        return False
