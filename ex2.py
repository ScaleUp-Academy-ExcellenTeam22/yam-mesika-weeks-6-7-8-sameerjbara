def group_by(func, iterable):
    """Returns a dictonary that the keys are the values that are returned from the passed function
       and the values of each key is list of all elements that retrund from the function
       the same value as the key
            Args:
                func (method): the function we will preform on each object in the iterable.
                iterable.
            Returns:
                dictonary: The grouped lists.
            Raises:
                none
            Examples:
                givin a list of strings and the len function
                will return a dictornary the the keys are the length of each string
                and the values are list of strings the the value of it equal the key.
                >>> print(group_by(len, ["hi", "bye"]))
                {2: ['hi'], 3: ['bye']}
            """
    print(type(func))
    grouped_lists = {func(element): [] for element in iterable}
    for element in iterable:
        grouped_lists[func(element)].append(element)
    return grouped_lists


print(group_by(len, ["hi", "hi", "bye", "fff", "ggg", "la"]))
