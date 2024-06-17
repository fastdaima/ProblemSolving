# two sum, 

# need to return indices where a+b = c , 
# we can check by creating an hash set,  where the key is c-a : index
# then we can reiterate the nums array, checking whether the value is in hash set and the index is different 
# if it satisfies the constraints, both the indexes are returned.
# 
from typing import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_set = {}
        for i, o in enumerate(nums): 
            rem = target - o 
            hash_set[rem] = i 

        for i, o in enumerate(nums):
            if o in hash_set and i != hash_set[o]: return [i, hash_set[o]]
         
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_set = {}
        for i, x in enumerate(nums):
            y = target-x
            if y in hash_set: return [i, hash_set[y]]
            hash_set[x] = i 
        
