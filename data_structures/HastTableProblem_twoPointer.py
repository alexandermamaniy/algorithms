from typing import List
# LeetCode Problem: https://leetcode.com/problems/two-sum/

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store numbers and their indices
        index_map = {}
        # Enumerate through the list of numbers
        for index, number in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - number
            # If complement is in the index_map, a solution is found
            if complement in index_map:
                # Return the indices of the two numbers
                return [index_map[complement], index]
            # Otherwise, add the current number and its index to the index_map
            index_map[number] = index
        # If no solution is found, this return will not be reached due to guaranteed solution.

    def my_twoSum(self, nums: list[int], target: int) -> list[int]:
        # print(nums)
        memo = {}  # O(1)
        for i in range(len(nums)):  # N
            if not nums[i] in memo.keys():
                memo[nums[i]] = []
            memo[nums[i]].append(i)

        nums = sorted(nums)  # N*L(N)
        # print(memo)
        # print(nums)
        # if  nums[0] > target:
        #     return [0, 0]

        left, right = 0, (len(nums) - 1)
        while right >= left:  # N
            if nums[right] + nums[left] > target:
                right -= 1
                print(left, right)
                continue
            if nums[right] + nums[left] == target:
                break
            else:
                left += 1
                print(left, right)

        if nums[left] == nums[right]:
            return memo[nums[left]]
        else:
            return [memo[nums[left]][0], memo[nums[right]][0]]

if __name__ == "__main__":
    s = Solution()

    nums = [2, 7, 11, 15]
    target = 9
    result = s.twoSum(nums, target)