#!/usr/bin/python3
"""Checking if all boxes can be opened"""


def canUnlockAll(boxes):
    """Method to check if all boxes can be opened"""
    if not boxes:
        return False
    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)
    if len(keys) == len(boxes):
        return True
    return False
