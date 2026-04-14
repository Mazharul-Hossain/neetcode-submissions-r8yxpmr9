class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        answer = 0
        while left <= right:
            # print(f"{left} => {height[left]}, {right} => {height[right]}, {left_max}, {right_max}")
            if left_max <= right_max:
                if left_max <= height[left]:
                    left_max = height[left]
                
                else:
                    answer += left_max - height[left]
                
                left += 1
                
            else:
                if right_max <= height[right]:
                    right_max = height[right]
                
                else:
                    answer += right_max - height[right]
                
                right -= 1

            # print(left, right, left_max, right_max, f"answer: {answer}")
        
        return answer

                 
