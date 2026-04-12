class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1]
        for _ in range(2, n + 1):
            dp.append(dp[-1] + dp[-2])
        
        return dp[n]
        