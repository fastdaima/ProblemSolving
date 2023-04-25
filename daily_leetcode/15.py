# Solution 1
# 1. sorting the list
# 2. filtering and sending values to twoSum function which are <=0 and arr[num]!=arr[num-1]
# (to avoid duplicate processing)
# because for this problem a + b +c = 0 which means a+b = -c, we are sending the
#-c value as target to twoSum function to find a + b
# 3. in twoSum function, declare next index variable as left, and last arr value
#as right, run the for loop, check arr[left] + arr[right] + arr[index] == 0
# if val found, add to result list, increment and decrement the pointers
# also run a for loop, to skip same arr[left] values
# if sum > 0 decrement right ptr, sum < 0 increment right pointer
# finally return the list
# [NOTE] here we already sorted the array at first, also we are declaring
# left and right pointers which comes after the index, so no separate sorting 
# is required 


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        out = []

        for i in range(0, len(nums)):
            if nums[i]<=0 and (i == 0 or nums[i]!=nums[i-1]):
                res = self.twoSum(nums, i, nums[i])
                for o in res: out.append(o)

        return out



    def twoSum(self, nums: List[int], index: int, target: int):
        out = []

        left = index + 1
        right = len(nums)-1

        while left < right:
            
            sum_ = nums[index] + nums[left] + nums[right]

            if sum_ == 0:
                out.append([nums[index], nums[left], nums[right]])
                left+=1
                right-=1

                while left < right and nums[left]==nums[left-1]:
                    left+=1
            elif sum_ > 0:
                right -= 1
            else:
                left += 1
        return out




# Solution 2
# 1. Sorting the array
# 2. converting threeSum problem to twoSum Problem
# 3. Sending -target to twoSum function, where using hash_map we populate 
# target-nums[index] = [nums[index], -target, target-nums[index]]
# is populated to the hash_map, checking whether the nums[index] value in 
# hash_map, if present then its mapped value is appended to the result list


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hash_set = set()
        nums = sorted(nums)
        output = []
        
        for ind in range(0, len(nums)-1):
            if ind > 0 and ind + 1 < len(nums) and nums[ind] == nums[ind+1]: continue

            result = self.twoSum(nums, ind, nums[ind]*-1)

            for res in result: 
                if tuple(res) not in hash_set:
                    hash_set.add(tuple(res))
                    output.append(res)
        
        return output        
        
    def twoSum(self, nums: List[int], target_index, target):
        hash_map = {}
        output = []

        for index in range(0, len(nums)):
            if index == target_index: continue

            if nums[index] in hash_map:
                output.append(sorted(hash_map[nums[index]]))
            else:
                hash_map[target-nums[index]] = [nums[index], -target, target-nums[index]]
        
        return output

            
        

        
            
