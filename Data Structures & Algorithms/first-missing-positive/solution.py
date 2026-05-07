class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        visited = set()

        for num in nums:
            if num > 0:
                visited.add(num)
        
        if len(visited) == 0:
            return 1
        
        max_num = max(visited)        
        for i in range(1, max_num + 2):
            if i not in visited:
                return i
        