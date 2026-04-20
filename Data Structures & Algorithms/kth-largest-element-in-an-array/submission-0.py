import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k  # convert to kth smallest

        def partition(left: int, right: int, pivot_index: int) -> int:
            pivot = nums[pivot_index]

            # move pivot to end
            nums[right], nums[pivot_index] = nums[pivot_index], nums[right]

            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[store_index] = nums[store_index], nums[i]
                    store_index += 1
                
            # move pivot to correct place
            nums[right], nums[store_index] = nums[store_index], nums[right]
            return store_index

        def quickSelect(left: int, right: int):
            while left < right:
                pivot_index = random.randint(left, right)
                correct_p_index = partition(left, right, pivot_index)

                if correct_p_index == k:
                    return nums[correct_p_index]
                
                elif correct_p_index < k:
                    left = correct_p_index + 1
                
                else:
                    right = correct_p_index - 1
            
            return nums[left]

        return quickSelect(0, len(nums) - 1)