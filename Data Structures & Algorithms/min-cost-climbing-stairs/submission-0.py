class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        for i in range(N):
            if i > 1:
                cost[i] += min(cost[i - 1], cost[i - 2])
            
            print(cost)
        
        return min(cost[N - 1], cost[N - 2])
