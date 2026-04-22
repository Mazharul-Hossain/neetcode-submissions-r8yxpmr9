class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = nums[0]
        cur_min, cur_max = 1, 1
        for n in nums:
            if n < 0:
                cur_min, cur_max = cur_max, cur_min

            cur_max = max(cur_max * n, n)
            cur_min = min(n, cur_min * n)

            answer = max(cur_max, answer)
        
        return answer