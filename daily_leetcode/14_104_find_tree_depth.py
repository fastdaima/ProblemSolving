
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
class Solution:
    
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0 
        
        def dfs(root, depth):
            if not root or (not root.right and not root.left): return depth 
            
            left = dfs(root.left, depth+1)if root.left else 0 
            right = dfs(root.right, depth+1 )if root.right else 0

            return max(left, right)
        
        return dfs(root, 0 ) + 1