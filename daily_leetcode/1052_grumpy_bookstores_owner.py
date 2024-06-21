class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], m: int) -> int:
        n = len(customers)
        unsatisfied = 0 
        for i in range(m):
            unsatisfied += customers[i]*grumpy[i]
        max_unsatisfied = unsatisfied 

        for i in range(m, n):
            unsatisfied += customers[i]*grumpy[i]
            unsatisfied -= customers[i-m]*grumpy[i-m]
            max_unsatisfied = max(unsatisfied, max_unsatisfied)
        
        for i in range(n):
            max_unsatisfied += customers[i]*(1-grumpy[i])
        
        return max_unsatisfied

        