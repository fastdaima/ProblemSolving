'''
1. find maxArea of rectangle
2. initialize 2 pointers, one pointing to index 0, another to last index and maxArea = -1
3. find area b/w lines using area = min(arr[l], arr[r])*(r-l)
here (r-l) stands for width, update maxArea if area is greater
4. if arr[l] < arr[r]: l+=1 move right
5. if arr[r] < arr[l]: r-=1 move left
6. return maxArea

'''


class Solution:
    def maxArea(self, h: List[int]) -> int:
        # l: left, r: right
        l = 0
        r = len(h)-1
        maxArea = -1

        while l < r:
            maxArea = max(maxArea, min(h[l], h[r])*(r-l))
            if h[l]<h[r]:
                l+=1 
            else:
                r-=1 
        return maxArea

