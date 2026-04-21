
        # Step 4: Base cases
        # Steal the first house
        dp[1] = nums[0]

        # Step 5: Order of computation
        # We compute from left --> right because we can take n only once
        for i in range(2, N + 1):

            # Step 3: Recurrence (transition)
            # At each step, I have two choices:
            #           leave it  or take it
            dp[i] = max(dp[i - 1], nums[i - 1] + dp[i - 2])
            
            # print(dp)            
        return dp[N]

    def rob(self, nums: List[int]) -> int:        
        # Step 1: Identify pattern: 
        # This looks like a DP problem because 
        # decisions at index i depend on previous subproblems.
        N = len(nums)
        # Let dp[i] represent how much we can steal at house i - 1?
        dp = [0] * (N + 1)
            
        # Step 2: Define state (MOST IMPORTANT)
            
        elif N == 1:
            return nums[0]
        if N == 0:
            return 0
        N = len(nums)
        
class Solution:
    def rob_I(self, nums: List[int]) -> int:        