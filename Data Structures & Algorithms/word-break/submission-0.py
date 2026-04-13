class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        N = len(s)

        dp = [False] * (N + 1)
        dp[0] = True

        for i in range(N + 1):
            for j in range(i):
                if dp[j] and s[j : i] in wordDict:
                    dp[i] = True
                    break
            # print(" \t ", " \t ".join(list(s)))
            # print(dp)
        
        return dp[N]