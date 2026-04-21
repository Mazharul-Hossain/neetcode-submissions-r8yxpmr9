        for c in word:
            if c not in head.children:
                head.children[c] = PrefixTreeNode()
            
            head = head.children[c]
        head.is_word =True
        

    def search(self, word: str) -> bool:
            for j in range(i, len(word)):
        def dfs_helper(i, head):
                c = word[j]