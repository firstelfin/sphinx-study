#!/usr/bin/env python3
# encoding: utf-8
# @author: firstelfin
# @time: 2024/02/07 15:30:48


def add_str(a: str, b: str) -> int:
    """
    :param a(str): 被加数;
    :param b(str): 加数;
    """
    return int(a) + int(b)


class DataItem(object):

    def __init__(self) -> None:
        pass

    def infer(self, a, b):
        return add_str(a, b)

