class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.answer = []

        def dfs(curr: str="", open_p: int=0, close_p: int=0) -> None:
            # 1. What am I building? curr: ""

            # 2. When do I stop?
            if len(curr) == 2 * n:
                self.answer.append(curr)
                return
            
            # What choices do I have? "(" or ")"
            if open_p < n:
                # What constraints prune invalid paths? open < n
                dfs(curr +  "(", open_p + 1, close_p)
            
            if close_p < open_p:
                # What constraints prune invalid paths? close < open
                dfs(curr +  ")", open_p, close_p + 1)
        
        dfs("", 0, 0)
        return self.answer