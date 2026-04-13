class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        # Step 1: Identify pattern: 
        # This looks like a DP problem because 
        # decisions at index i depend on previous subproblems.

        # Step 6: Optimization
        # Using 1D DP instead of 2D
        
        # Step 7: Complexity 
        # - Time: O(N * target)
        # - Space O(target)
        """
        N = len(nums)
        total_sum = sum(nums)

        # If total is odd → impossible
        if total_sum % 2:
            return False
        target = total_sum // 2

        # Step 2: Define state
        # Let dp[i] represent if we can form sum s?
        dp = [False] * (target + 1)
        # Step 4: Base cases, sum 0 is always possible
        dp[0] = True

        # Step 5: Order of computation
        for n in nums:
            # We compute from left <-- right because we can take n only once
            for i in range(target, n - 1, -1):

                # Step 3: Recurrence (transition)
                # At each step, I have two choices:
                #       leave it    or take it
                dp[i] = dp[i] or dp[i - n]
            
            if dp[target]:
                return True
        
        return dp[target]