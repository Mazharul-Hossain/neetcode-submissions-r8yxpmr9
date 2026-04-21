class PrefixTreeNode:
    def __init__(self, is_word=False):
        self.is_word = is_word
        self.children = {}
        
class WordDictionary:

    def __init__(self):
        self.root = PrefixTreeNode()
        

    def addWord(self, word: str) -> None:
        head = self.root
        for c in word:
            if c not in head.children:
                head.children[c] = PrefixTreeNode()
            
            head = head.children[c]
        head.is_word =True
        

    def search(self, word: str) -> bool:
        def dfs_helper(i, head):
            for j in range(i, len(word)):
                c = word[j]
                if c == ".":
                    for child in head.children.values():
                        if dfs_helper(j + 1, child):
                            return True
                    return False
                else:
                    if c not in head.children:
                        return False                    
                    head = head.children[c]

            return head.is_word        
        
        return dfs_helper(0, self.root)
        
