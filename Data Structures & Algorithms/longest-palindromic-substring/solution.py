        # print(dp)

        ans_indx, ans_len = 0, 0
        # Step 5: Order of computation
        # We compute from left --> right and top <-- bottom because we can take compute substrings only once
        for i in range(N - 1, -1, -1):
            # Step 4: Base cases
            # each letter is 1 len palindrom

            for j in range(i, N):
                # Step 3: Recurrence (transition)
                # At each step, I have one choices:
                # s[i:j] is a palindrome if:
                # print(i + 1, j - 1)
                # 1. s[i] == s[j]
                # 2. the inner substring s[i+1:j-1] is also a palindrome
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    temp_len = j - i + 1
        # Let dp[i] represent how much we can steal at house i - 1?
        dp = [[False for _ in range(N)] for _ in range(N)]
            return s
            
        # Step 2: Define state (MOST IMPORTANT)
            
        elif N == 1:
        if N == 0:
            return ""
        # decisions between index i and j depend on previous subproblems.
        N = len(s)
        
        # Step 1: Identify pattern: 
        # This looks like a DP problem because 
class Solution:
    def longestPalindrome(self, s: str) -> str:  