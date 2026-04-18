class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in ["+", "-", "*", "/"]:
                b = stack.pop()
                if c == "+":
                    stack[-1] += b
                elif c == "-":
                    stack[-1] -= b
                elif c == "*":
                    stack[-1] *= b
                elif c == "/":
                    stack[-1] = int(stack[-1] / float(b))
            else:
                stack.append(int(c))
            # print(stack)
        return stack[0]
        