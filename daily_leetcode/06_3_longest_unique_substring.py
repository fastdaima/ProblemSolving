

# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# init left and right pointers

# create a set for adding new variables 

# iterate the string 

# if char is present in set: 
#     then remove char from set
#     increase left by 1 

# then add char to set 

# then calculate max_length = max(max_length, right - left + 1)





class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
       
        left = 0       
        
        max_len = 0 

        seen = set()

        unique = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1 
            seen.add(s[right])
            max_len = max(max_len, right-left+1)

        return max_len
