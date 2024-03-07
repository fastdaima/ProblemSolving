# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


# init 2 pointers left and right 
# calculate the distance between the pillars - heights
# move the pointer closer or decrease the pointer where it corresponding height is less 
# left -- if h[left]< h[right] else right --
# the reason is simple
# whenever you decrease the pointer 
# the width is gonah decrease 
# and we can confidently say that max_area will not be attained if we move the pointer where height is greater. 


class Solution:
    def maxArea(self, h: List[int]) -> int:
        max_area = 0

        left = 0
        right = len(h)-1

        while left < right:
            index_diff = right -left 
            
            # distance 
            d = min(h[left], h[right])

            max_area = max(d*index_diff, max_area)

            if h[left] < h[right]:
                left += 1
            else:
                right -= 1
            
        return max_area