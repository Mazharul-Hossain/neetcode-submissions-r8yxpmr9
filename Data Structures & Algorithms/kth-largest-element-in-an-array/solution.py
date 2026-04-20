                    store_index += 1
                if nums[i] < pivot:
                    nums[i], nums[store_index] = nums[store_index], nums[i]

            store_index = left
            for i in range(left, right):
            # move pivot to end
            nums[right], nums[pivot_index] = nums[pivot_index], nums[right]
            pivot = nums[pivot_index]


        def partition(left: int, right: int, pivot_index: int) -> int:
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k  # convert to kth smallest


import random
                
            # move pivot to correct place
            nums[right], nums[store_index] = nums[store_index], nums[right]
            return store_index

        def quickSelect(left: int, right: int):
            while left <= right:
                # pivot_index = random.randint(left, right)
                pivot_index = (left + right) // 2
                c_pivot_index = partition(left, right, pivot_index)

                if c_pivot_index == k:
                    return nums[c_pivot_index]
                
                elif c_pivot_index < k:
                    left = c_pivot_index + 1
                