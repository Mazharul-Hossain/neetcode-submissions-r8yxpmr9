class Solution:
    def countSubstrings(self, s: str) -> int:
        # Step 1: Identify pattern: 
        # This looks like a DP problem because 
        # decisions between index i and j depend on previous subproblems.
        N = len(s)
        
        # if N == 0:
        #     return ""
            
        # elif N == 1:
        #     return s
            
        # Step 2: Define state (MOST IMPORTANT)
        # Let dp[i] represent how much we can steal at house i - 1?
        dp = [[False for _ in range(N)] for _ in range(N)]
        # print(dp)

        answer = 0
        # Step 5: Order of computation
        # We compute from left --> right and top <-- bottom because we can take compute substrings only once
        for i in range(N - 1, -1, -1):
            # Step 4: Base cases
            # each letter is 1 len palindrom

            for j in range(i, N):
                # Step 3: Recurrence (transition)
                # At each step, I have one choices:
                # palindrom and previous also palindrom
                # print(i + 1, j - 1)
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    answer += 1
                    # temp_len = j - i + 1
                    # if ans_len < temp_len:
                    #     ans_indx = i
                    #     ans_len = temp_len
            
            # print(dp)
            # print()

        # Step 6: Optimization
        # Using 1D DP
        # Step 7: Complexity 
        # - Time: O(N * N)
        # - Space O(N * N)

        # return s[ans_indx: ans_indx + ans_len]
        return answer

        