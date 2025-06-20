#!/usr/bin/python3
from fundametal_maths.my_maths import sum_of_arithmetic_sequence, is_geometric_sequence

if __name__ == "__main__":
    # Example usage of sum_of_arithmetic_sequence
    array = [2, 4, 6, 8, 10]
    result = sum_of_arithmetic_sequence(array)
    print(f"The sum of the arithmetic sequence {array} is: {result}")


    # Test cases for sum_of_arithmetic_sequence
    print(is_geometric_sequence([2, 6, 18, 54]))  # True
    print(is_geometric_sequence([1, 2, 4, 8]))  # True
    print(is_geometric_sequence([1, 2, 6]))  # False