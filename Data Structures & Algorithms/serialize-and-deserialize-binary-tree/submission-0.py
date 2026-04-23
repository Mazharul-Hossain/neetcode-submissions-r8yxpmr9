# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.answer = []
        
        def dfs(node):
            if not node:
                self.answer.append("#")
                return
            self.answer.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(self.answer)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        self.index = -1

        def dfs():
            self.index += 1
            if nodes[self.index] == "#":
                return None
            
            node = TreeNode(int(nodes[self.index]))
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()