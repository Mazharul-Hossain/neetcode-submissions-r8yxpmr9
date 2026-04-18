class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        L = len(temperatures) 
        answer = [0] * L

        mono_stack = []
        for i, temp in enumerate(temperatures):
            while mono_stack and mono_stack[-1][0] < temp:
                j = mono_stack[-1][1]
                answer[j] = i - j
                _ = mono_stack.pop()

            mono_stack.append((temp, i))
            # print(i, temp, mono_stack)
        
        return answer