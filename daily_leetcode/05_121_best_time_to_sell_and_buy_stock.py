
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Algorithm 
# we can't buy and sale on same day , profit = 0
# you can be sure that if the current price is the cheapest price, then you can't calculate max profit,
# if current price is greater than the cheapest price, then you know for sure that it is not an cheapest price 

# if check whether current price is the cheapest you have ever seen:
#     update your cheapest price 
# elif if you find current_price - cheapest price greater than max_profit:
#     then max_proft = current_price - cheapest price 




class Solution:
    def maxProfit(self, p: List[int]) -> int:
        
        is_cheapest_one = float('inf')
        max_profit = 0 

        for i in range(len(p)):
            if p[i] < is_cheapest_one: is_cheapest_one = p[i]
            elif p[i]-is_cheapest_one > max_profit: max_profit = p[i]-is_cheapest_one
            
        return max_profit

            
            