class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        answer = 0

        stack = []
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                start, h = stack.pop()
                # print(f"({i} - {start}) * {h} = {(i - start) * h}, {answer}")
                answer = max((i - start) * h, answer)

            stack.append((start, height))
        
        for i, h in stack:
            answer = max((len(heights) - i) * h, answer)
        
        return answer
        