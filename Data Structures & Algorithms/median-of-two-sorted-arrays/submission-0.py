class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        M_end, N_end = len(nums1), len(nums2)
        M_start, N_start = 0, 0

        median1 = median2 = 0
        middle = (M_end + N_end) // 2 + 1
        for _ in range(middle):
            median2 = median1

            if M_start < M_end and N_start < N_end:
                if nums1[M_start] <= nums2[N_start]:
                    median1 = nums1[M_start]
                    M_start += 1
                
                else:
                    median1 = nums2[N_start]
                    N_start += 1
            
            elif M_start < M_end:
                median1 = num1[M_start]
                M_start += 1
            
            else:
                median1 = nums2[N_start]
                N_start += 1
        
        if (M_end + N_end) % 2:
            return float(median1)
        
        return (median2 + median1) / 2.0


