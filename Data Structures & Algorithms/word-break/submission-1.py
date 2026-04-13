class TreeNonde:
    def __init__(self):
        self.childer = {}
        self.is_word = False

class Solution:
    def __init__(self):
        self.root = TreeNonde()
    
    def insert(self, word):
        head = self.root
        for w in word:
            if w not in head.childer:
                head.childer[w] = TreeNonde()
            head = head.childer[w]
        head.is_word = True

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # wordDict = set(wordDict)
        for word in wordDict:
            self.insert(word)

        N = len(s)

        dp = [False] * (N + 1)
        dp[0] = True

        for i in range(N + 1):
            for j in range(i):
                # if dp[j] and s[j : i] in wordDict:
                if dp[j]:
                    found = True
                    head = self.root
                    for k in range(j, i):
                        if s[k] not in head.childer:
                            found = False
                            break
                        head = head.childer[s[k]]
                    
                    if found and head.is_word:
                        dp[i] = True
                        break

            # print(" \t ", " \t ".join(list(s)))
            # print(dp)
        
        return dp[N]