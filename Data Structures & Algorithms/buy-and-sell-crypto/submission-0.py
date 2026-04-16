class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_cost = prices[0]

        for price in prices:
            if max_profit < price - min_cost:
                max_profit = price - min_cost
            
            if price < min_cost:
                min_cost = price
        
        return max_profit
        