class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            # (l + r) // 2 can lead to overflow
            mid = left + ((right - left) // 2)
            
            if nums[mid] < target:
                left = mid + 1
            
            elif nums[mid] > target:
                right = mid - 1
            
            else:
                return mid

        return -1