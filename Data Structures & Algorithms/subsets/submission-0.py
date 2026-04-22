class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.answer = []

        def dfs(i=0, subset=[]):
            # print(subset)
            self.answer.append(subset.copy())

            for j in range(i, len(nums)):
                subset.append(nums[j])
                dfs(j + 1, subset)
                subset.pop()
        
        dfs()
        return self.answer