# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        q = deque([root])

        while q:
            # rightSide = None
            # print(q, q[-1].val)
            res.append(q[-1].val)
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    # rightSide = node
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            # if rightSide:
            #     res.append(rightSide.val)
        return res
        