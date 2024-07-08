#!/usr/bin/python3
"""
function that calculates the minimum number of operations needed
to result in exactly n H characters in the file
"""


def minOperations(h):
    """
    function that calculates the minimum number of operations needed
    to result in exactly n H characters in the file
    """
    if not isinstance(h, int) or h <= 0:
        return 0
    copy_var = 1
    rep_var = 1
    op_count = 0
    while rep_var < h:
        if h % rep_var == 0:
            copy_var = rep_var
            rep_var *= 2
            op_count += 2
        else:
            rep_var += copy_var
            op_count += 1
    return op_count
