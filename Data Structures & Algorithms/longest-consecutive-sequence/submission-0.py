class TreeNode:
    def __init__(self, val):
        self.parent = val
        self.rank = 1

class Solution:
    def find(self, a):
        if a != self.hash_map[a].parent:
            self.hash_map[a].parent = self.find(self.hash_map[a].parent)
        
        return self.hash_map[a].parent


    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)

        if parent_a == parent_b:
            return None

        if parent_a <= parent_b:

            self.hash_map[parent_b].parent = parent_a
            self.hash_map[parent_a].rank += self.hash_map[parent_b].rank

        else:            
            self.hash_map[parent_a].parent = parent_b
            self.hash_map[parent_b].rank += self.hash_map[parent_a].rank

    def longestConsecutive(self, nums: List[int]) -> int:
        self.hash_map = {}
        
        answer = 0
        for n in nums:
            if n in self.hash_map:
                continue
            
            self.hash_map[n] = TreeNode(n)
            if n - 1 in self.hash_map:
                self.union(n - 1, n)
            
            if n + 1 in self.hash_map:
                self.union(n, n + 1)

            parent = self.find(n)
            answer = max(answer, self.hash_map[parent].rank)
        
        return answer
            
