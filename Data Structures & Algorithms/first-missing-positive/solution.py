class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        visited = set()

        for num in nums:
            if num >= 0:
                visited.add(num)
        
        min_num, max_num = min(visited), max(visited)
        if len(visited) == max_num + 1 - min_num:
            return max_num + 1
        
        for i in range(min_num + 1, max_num):
            if i not in visited:
                return i
        