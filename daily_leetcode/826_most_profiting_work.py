class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        worker.sort(reverse=True)

        total_profit = 0 

        heap = [(-p,d) for d,p in zip(difficulty, profit)]
        heapify(heap)

        for w in worker: 
            while heap and heap[0][1]>w:
                heappop(heap)
            if not heap: 
                break 
            total_profit += heap[0][0]
        return -total_profit
        
        # # diff_profit_map
        # hm = dict() 

        # total_profit = 0
        
        # for d,p in zip(difficulty, profit):
        #     hm[d] = max(hm.get(d,0), p)
        
        # hm = { a:b for a,b in sorted(hm.items(), key = lambda x: x[0]) }

        # worker = sorted(worker)

        # for w in worker: 
        #     max_profit = 0
            
        #     for k,v in hm.items(): 
        #         if k <= w: 
        #             max_profit = max(max_profit, v)
        #         elif k==w: 
        #             break
        #         else:
        #             break 
                
        #     total_profit += max_profit
        # return total_profit






