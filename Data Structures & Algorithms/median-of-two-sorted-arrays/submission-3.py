class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        M_end, N_end = len(nums1), len(nums2)
        middle = (M_end + N_end + 1) // 2

        left, right = 0, M_end
        while left <= right:
            # Take i count of elements from nums1
            i = (left + right) // 2
            # Take j count of elements from nums2
            j = middle - i

            # Everything on the left <= everything on the right
            # nums1: [ ... i elements | rest ] so nums1[i-1] <= nums2[j]
            M_left = float("-inf") if i == 0 else nums1[i-1]
            N_right = float("inf") if j == N_end else nums2[j]

            # nums2: [ ... j elements | rest ] so nums2[j-1] <= nums1[i]
            N_left = float("-inf") if j == 0 else nums2[j-1]
            M_right = float("inf") if i == M_end else nums1[i] 

            if M_left <= N_right and N_left <= M_right:
                if (M_end + N_end) % 2:
                    return max(M_left, N_left)
                else:
                    return (max(M_left, N_left) + min(M_right, N_right)) / 2.0
            
            elif M_left > N_right:
                # An element from nums1 LEFT side is too big
                # it should actually be on the RIGHT side
                right = i - 1
            
            else:
                left = i + 1



