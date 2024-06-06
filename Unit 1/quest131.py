def intersection(list_1, list_2):
    """
    Finds the elements that are present in both lists.

    Args:
        list_1: The first list.
        list_2: The second list.

    Returns:
        A new list containing the unique elements found in both input lists.
    """

    my_list = [x for x in list_1 if x in list_2]
    return list(set(my_list))


print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))
