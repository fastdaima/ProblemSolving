import heapq
from typing import List 

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)

        capital_profit = sorted([[a,b] for a,b in zip(capital, profits)])

        heap = []
        last = -1 

        for i in range(n):
            cap, prof = capital_profit[i]
            
            if cap <= w: 
                heapq.heappush(heap, -prof)
                print(heap)
            else: 
                last = i 
                break 

        
        while k and heap: 
            w += - heapq.heappop(heap)
            k -= 1

            while last < n and capital_profit[last][0] <= w: 
                heapq.heappush(heap, -capital_profit[last][1])
                print(heap)
                last += 1
        
        return w 








inputs = [
    [2, 0, [1,2,3], [0,1,1]],
    [3, 0, [1,2,3], [0,1,2]]
]


s = Solution() 

for o in inputs: 
    print(s.findMaximizedCapital(*o))


# if __name__ =='__main__' :
#     with open('user.out', 'w') as f :
#         for k, w, profits, capital in zip(map(loads, stdin), map(loads, stdin), map(loads, stdin), map(loads, stdin)) :
#             print(findMaximizedCapital(k, w, profits, capital), file = f)
#     exit()