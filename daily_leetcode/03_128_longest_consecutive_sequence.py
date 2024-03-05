from typing import List

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# optimized 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_set_length = 0 
        hash_set = set(nums)

        for num in hash_set:
            if num-1 not in hash_set:
                next_num = num+1 

                while next_num in hash_set:
                    next_num += 1 
                
                max_set_length = max(max_set_length, next_num - num )

                # here next_num - num, denotes the total_sum and the number it has started with
        
        return max_set_length

# sol 2 


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_set_length = 0 
        hash_set = set(nums)

        for num in hash_set:
            if num-1 not in hash_set:
                current_num = num 
                current_set_length = 1

                while current_num + 1 in hash_set:
                    current_num += 1
                    current_set_length += 1
                
                max_set_length = max(max_set_length, current_set_length)
        
        return max_set_length


s = Solution()

inputs =  [[100,4,200,1,3,2], [0,3,7,2,5,8,4,6,0,1]]

for inp in inputs:
    print(s.longestConsecutive(inp))
                

                    





