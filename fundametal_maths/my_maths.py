#!/usr/bin/python3

def sum_of_arithmetic_sequence(array: list[int]) -> int:
    """ The array must be sorted and be an arithmetic sequence """
    first_element = array[0]
    last_element = array[-1]
    n = len(array)
    return n * (first_element + last_element) // 2


def is_geometric_sequence(array: list[int]) -> bool:
    # Base cases
    if len(array) <= 2:
        return True  # Any array of length 0, 1, or 2 forms a geometric sequence

    # Calculate the ratio between the first two elements
    if array[0] == 0:
        return False  # Avoid division by zero

    ratio = array[1] / array[0]

    # Check if the ratio between the next pair is the same
    if array[2] / array[1] != ratio:
        return False

    # Recursive call
    return is_geometric_sequence(array[1:])