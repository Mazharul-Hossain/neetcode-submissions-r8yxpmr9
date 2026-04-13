class TreeNonde:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def __init__(self):
        self.root = TreeNonde()
    
    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TreeNonde()
            node = node.children[w]
        node.is_word = True
    
    def search(self, s, i, j):
        node = self.root
        for idx in range(i, j + 1):
            if s[idx] not in node.children:
                return False
            node = node.children[s[idx]]
        return node.is_word

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # wordDict = set(wordDict)
        for word in wordDict:
            self.insert(word)

        N = len(s)

        dp = [False] * (N + 1)
        # empty suffix is always valid
        dp[N] = True

        for i in range(N - 1, -1, -1):
            for j in range(i, N):
                # if dp[j] and s[j : i] in wordDict:
                if dp[j + 1] and self.search(s, i, j):
                    dp[i] = True
                    break

            # print(" \t ", " \t ".join(list(s)))
            # print(dp)
        
        return dp[0]