class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                b = stack.pop()
                stack[-1] += b
            elif c == "-":
                b = stack.pop()
                stack[-1] -= b
            elif c == "*":
                b = stack.pop()
                stack[-1] *= b
            elif c == "/":
                b = stack.pop()
                stack[-1] = int(stack[-1] / float(b))
            else:
                stack.append(int(c))
            # print(stack)
        return stack[0]
        