            dfs(node.right)
            self.answer.append(str(node.val))
            dfs(node.left)
                return

        dfs(root)
        return ",".join(self.answer)
            if not node:
                self.answer.append("#")
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        self.index = -1

        def dfs():
            self.index += 1
            if nodes[self.index] == "#":
                return None
            
            node = TreeNode(int(nodes[self.index]))
        self.answer = []
        
        def dfs(node):
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
class Codec:
    