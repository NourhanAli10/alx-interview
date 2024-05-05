#!/usr/bin/python3
"""0-lockboxes.py"""

def canUnlockAll(boxes):
    # Set to keep track of unlocked boxes
    unlocked = {0}
    # List to keep track of keys that need to be checked
    keys_to_check = boxes[0]
    
    while keys_to_check:
        # Get a key from the list of keys to check
        key = keys_to_check.pop()
        # If the key opens a box that hasn't been unlocked yet
        if key < len(boxes) and key not in unlocked:
            # Add the key to the set of unlocked boxes
            unlocked.add(key)
            # Add the keys from the newly unlocked box to the list of keys to check
            keys_to_check.extend(boxes[key])
    
    # If all boxes have been unlocked
    if len(unlocked) == len(boxes):
        return True
    else:
        return False