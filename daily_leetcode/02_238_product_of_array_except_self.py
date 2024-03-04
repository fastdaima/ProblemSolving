# 238. Product of Array Except Self
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]





class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_of_zeros = 0 
        zero_indices = []
        prod = 1

        for i, o in enumerate(nums): 
            if o == 0: 
                num_of_zeros += 1
                zero_indices.append(i)
            else:
                prod *= o


        if num_of_zeros > 1: return [0 for o in nums]

        if num_of_zeros == 1:
            out = [0 for o in nums]
            out[zero_indices[0]] = prod
            return out 

        out = [prod//o for o in nums]
        return out
        


        