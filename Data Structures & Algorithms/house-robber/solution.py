class Solution:
    def rob(self, nums: List[int]) -> int:        
        N = len(nums)
        dp = [0] * (N + 1)
        for i in range(1, N + 1):
            if i == 1:
                dp[i] = nums[i - 1]

            else:
                dp[i] = max(dp[i - 1], nums[i - 1] + dp[i - 2])
            
            print(dp)
        
        return dp[N]