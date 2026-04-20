class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.answer = []

        def dfs(curr: str="", open_p: int=0, close_p: int=0) -> None:

                self.answer.append(curr)
            
            # What choices do I have? "(" or ")"
            
            # 1. What am I building? curr: ""
            # 2. When do I stop?
            if len(curr) == 2 * n:
                return
            if open_p < n:
                dfs(curr +  "(", open_p + 1, close_p)
                # What constraints prune invalid paths? open < n
            if close_p < open_p:
                # What constraints prune invalid paths? close < open
                dfs(curr +  ")", open_p, close_p + 1)
        
        dfs("", 0, 0)
        return self.answer