from collections import defaultdict
from typing import Callable


def group_by(func: Callable[[iter], str or int], iterable: iter) -> defaultdict:
    """
    create a defaultdict when all each key is a list of all object that share the same return value and
    the key is all the values that return from the given function
    @:param func: the given function , iterable : the iterable object
    @:return defaultdict: the result dict

    """
    grouped_lists = defaultdict(list)
    for element in iterable:
        grouped_lists[func(element)].append(element)
    return grouped_lists


group_by(len, ["hi", "hi", "bye", "fff", "ggg", "la"])

