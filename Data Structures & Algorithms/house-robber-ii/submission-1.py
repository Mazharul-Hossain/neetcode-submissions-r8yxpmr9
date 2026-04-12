class Solution:
    def rob(self, nums: List[int]) -> int:        
        # Step 1: Identify pattern: 
        # This looks like a DP problem because 
        # decisions at index i depend on previous subproblems.
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[length - 1]

        
        def helper(left: int, right: int) -> int:        
            N = right + 1
            # Step 2: Define state (MOST IMPORTANT)
            # Let dp[i] represent how much we can steal at house i - 1?
            dp = [0] * (N + 1)

            # Step 5: Order of computation
            for i in range(left + 1, N + 1):
                # We compute from left --> right because we can take n only once

                if i - 1 == left:
                    # Step 4: Base cases
                    # Steal the first house
                    dp[i] = nums[i - 1]

                else:
                    # Step 3: Recurrence (transition)
                    # At each step, I have two choices:
                    #             leave it    or take it
                    dp[i] = max(dp[i - 1], nums[i - 1] + dp[i - 2])
                
                # print(dp)            
            return dp[N]

        # Step 6: Optimization
        # Using 1D DP instead of 2D        
        # Step 7: Complexity 
        # - Time: O(N * 2)
        # - Space O(N * 2)

        return max(helper(0, length - 2), helper(1, length - 1) )