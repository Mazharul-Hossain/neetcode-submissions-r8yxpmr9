import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        
        dp = [1] * N
        lsi_subsequence = []

        for n in nums:
            pos = bisect.bisect_left(lsi_subsequence, n)
            if pos >= len(lsi_subsequence):
                lsi_subsequence.append(n)
            
            else:
                lsi_subsequence[pos] = n
            
            # print(lsi_subsequence)
        
        return len(lsi_subsequence)