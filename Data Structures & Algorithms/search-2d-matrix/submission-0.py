class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])

        left, right = 0, M * N - 1
        while left <= right:
            mid = left + (right - left) // 2
            x, y = mid // N, mid % N

            if matrix[x][y] < target:
                left = mid + 1
            
            elif matrix[x][y] > target:
                right = mid - 1
            
            else:
                return True
            
        return False

        