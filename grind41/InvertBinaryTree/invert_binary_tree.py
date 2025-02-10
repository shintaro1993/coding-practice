class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        node = TreeNode(root.val)
        node.right = self.invertTree(root.left)
        node.left = self.invertTree(root.right)
        return node
