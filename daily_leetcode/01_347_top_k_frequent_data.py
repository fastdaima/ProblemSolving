# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 


class Solution:
    def topKFrequent(self, nums: List[int], t: int) -> List[int]:
        out = []
        hash_map = {}
        for o in nums: 
            if o in hash_map: hash_map[o] += 1
            else: hash_map[o] = 1
        
        return list(dict(sorted(hash_map.items(), key = lambda k: k[1], reverse=True)).keys())[:t]