        q = deque([root])

        while q:
            # rightSide = None
            # print(q, q[-1].val)
        res = []
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
class Solution:
#         self.left = left
#         self.right = right

#         self.val = val
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
# Definition for a binary tree node.
        if not root:
            return res

            res.append(q[-1].val)
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    # rightSide = node
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            # if rightSide:
            #     res.append(rightSide.val)
        return res
        