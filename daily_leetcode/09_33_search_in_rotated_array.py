
# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1


# my solution n/2

class Solution:
    def search(self, arr: List[int], t: int) -> int:
        
        if t not in arr: return -1

        l, r = 0, len(arr)-1

        while l < len(arr) and r >-1:
            print(l, r)
            if arr[l] == t: return l 
            elif arr[r] == t: return r 
            elif arr[l] < t: l+=1 
            else: r-=1
        
        return 0








"""
[1,2,3,4,5] -> basic binary search

left of pivot element is decreasing
right of pivot element is increasing
[5,1,2,3,4]
[4,5,1,2,3]
[3,4,5,1,2]
[2,3,4,5,1]
"""

# optimized solution from discussion

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        left, right = 0, len(nums)-1

        if nums[left] < nums[right] and (target < nums[left] or target > nums[right]):
            return -1
        
        while left <= right:
            if target == nums[left]:
                return left
            if target == nums[right]:
                return right
                
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # Check if mid is pivot point
            if nums[left] > nums[mid]: # mid --> right is increasing
                if target > nums[mid]:
                    if target > nums[right]:
                        right = mid - 1 
                    else:
                        left = mid + 1
                else:
                    right = mid - 1
            else: # left --> mid is increasing
                if target > nums[mid]:
                    left = mid + 1
                else:
                    if target > nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1
        return -1

