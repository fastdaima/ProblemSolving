# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false


class Solution:
    def isValid(self, s: str) -> bool:
        struct = {
            '[': ']', '(': ')', '{':'}'
        }

        stack = []

        for ch in s:
            if ch in struct:
                stack.append(ch)
            elif ch in struct.values():
                if not stack or struct[stack.pop()] != ch:
                    return False 
        
        return not stack

