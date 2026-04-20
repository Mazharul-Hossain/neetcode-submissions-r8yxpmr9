class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.answer = []

        def dfs(start: int, curr: List[int]):

            # print(f"{start}: {nums[start]}", curr)
            self.answer.append(curr.copy())
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                curr.append(nums[i])
                dfs(i + 1, curr) # reuse not allowed
                curr.pop()
        
        dfs(0, [])
        return self.answer