"""Step1


"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            if node.val > max(p.val, q.val):
                stack.append(node.left)
                continue
            if node.val < min(p.val, q.val):
                stack.append(node.right)
                continue
            return node
        return None
ls

        