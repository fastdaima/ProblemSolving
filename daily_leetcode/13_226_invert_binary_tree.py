
# Given root of binary tree, invert the tree and return the root 

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root: 
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root

