#!/usr/bin/python3

"""
optimisation is needed to be considered
and readability changes to be reviewed
"""


def canUnlockAll(boxes):
    check = True
    progress = {
        0: 0
    }
    current = [0]

    while len(progress) <= len(boxes) - 1 and check is True:
        if len(current) > 0:
            key = current.pop()
            if len(boxes[key]) > 0:
                for i in boxes[key]:
                    if i < len(boxes):
                        if i not in progress:
                            progress.update({i: i})
                            current.insert(len(current), i)
            else:
                if len(current) == 0 and len(progress) < len(boxes):
                    check = False
        else:
            if len(progress) < len(boxes):
                check = False
    return (check)
