class PrefixTreeNode:
    def __init__(self, is_word=False):
        self.is_word = is_word
        self.children = {}
    
class PrefixTree:

    def __init__(self):
        self.root = PrefixTreeNode()

    def insert(self, word: str) -> None:
        head = self.root
        for c in word:
            if c not in head.children:
                head.children[c] = PrefixTreeNode()
            
            head = head.children[c]
        head.is_word =True

    def search(self, word: str) -> bool:
        head = self.root
        for c in word:
            if c not in head.children:
                return False
            
            head = head.children[c]
        return head.is_word