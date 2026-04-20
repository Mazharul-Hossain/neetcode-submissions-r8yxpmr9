class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.answer = []

        def dfs(start: int, curr: List[int], remaining: int):

            # print(f"{start}: {candidates[start]}", curr, remaining)
            if remaining == 0:
                self.answer.append(curr.copy())
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if remaining < candidates[i]:
                    break
                
                curr.append(candidates[i])
                dfs(i + 1, curr, remaining - candidates[i]) # reuse not allowed
                curr.pop()
        
        dfs(0, [], target)
        return self.answer