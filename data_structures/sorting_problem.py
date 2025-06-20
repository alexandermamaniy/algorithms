# https://leetcode.com/problems/array-partition/submissions/1670934372/

from typing import List

class Solution:

    def arrayPairSum(self, nums: List[int]) -> int:
        """
        Find the max sum of min pairs in an array.
        The function takes in an array of 2n integers and we need to pair them up
        in such a way to minimize the difference between the pairs. The sum we want
        to maximize is the sum of the smaller number in each pair.
        :param nums: List[int] - Array of 2n integers
        :return: int - Maximum sum of min pairs
        """

        # Sort the array in non-decreasing order
        sorted_nums = sorted(nums)
        # Take every other element starting from the first element
        # because after sorting, the first element of each pair
        # will be the smaller one
        min_pairs_sum = sum(sorted_nums[::2])
        return min_pairs_sum

# Example usage:
# sol = Solution()
# print(sol.arrayPairSum([1,4,3,2]))  # Output: 4