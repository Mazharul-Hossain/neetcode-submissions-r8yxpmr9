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

        def helper(left, right, preorder_index=0):
            if left > right:
                return None
            
            root_val = preorder[preorder_index]
            root = TreeNode(root_val)

            root_idx = inorder_index[root_val]

            root.left = helper(left, root_idx - 1, preorder_index + 1)
            root.right = helper(root_idx + 1, right, preorder_index + 1 + root_idx - left)

            return root
        
        return helper(0, len(inorder) - 1)

            

        