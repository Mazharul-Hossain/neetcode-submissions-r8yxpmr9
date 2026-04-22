class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = nums[0]
        cur_min, cur_max = 1, 1
        for n in nums:
            temp_max = max(cur_max * n, n, cur_min * n)
            cur_min = min(cur_max * n, n, cur_min * n)
            cur_max = temp_max

            answer = max(cur_max, answer)
        
        return answer

