
        def dfs(i=0, subset=[]):
            self.answer.append(subset.copy())

            for j in range(i, len(nums)):
                subset.append(nums[j])
                dfs(j + 1, subset)
            # print(subset)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
                subset.pop()
        
        dfs()
        return self.answer