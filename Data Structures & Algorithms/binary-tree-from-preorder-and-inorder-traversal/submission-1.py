# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder = [root, left side, right side]
        # inorder = [left side, root, right side]
        inorder_index = {v: i for i, v in enumerate(inorder)}
        self.preorder_index = 0

        def dfs(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.preorder_index]
            self.preorder_index += 1
            root_idx = inorder_index[root_val]

            root = TreeNode(root_val)
            root.left = dfs(left, root_idx - 1)
            root.right = dfs(root_idx + 1, right)

            return root
        
        return dfs(0, len(inorder) - 1)