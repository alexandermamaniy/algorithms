# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty list to use as a stack
        stack = []
        # Create a set with valid parentheses pairs
        valid_pairs = {'()', '[]', '{}'}
        # Iterate over each character in the string
        for char in s:
            # If the character is an opening parenthesis, push it onto the stack
            if char in '({[':
                stack.append(char)
            # If the stack is empty or the formed pair is not valid, return False
            elif not stack or stack.pop() + char not in valid_pairs:
                return False

        # If the stack is empty, all parentheses were valid and correctly nested
        return not stack


if __name__ == "__main__":

    solution = Solution()
    print(solution.isValid("()[]{}"))       # True
    print(solution.isValid("(]"))           # False
    print(solution.isValid("["))            # False
