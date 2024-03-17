# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# construct inorder traversal push vals to list, then validate the list
# parallel parsing approach

class Solution:
    
    def preorder_traversal(self, root, out=[]):
        if root: 
            print(root.val)
            out.append(root.val)
            self.preorder_traversal(root.left, out)
            self.preorder_traversal(root.right, out)
        else:
            print(None)
            out.append(None)
        return out
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        left = self.preorder_traversal(p, [])
        right = self.preorder_traversal(q, [])

        return left == right


# using dfs

class Solution:

    def dfs(self, p, q):
        if p is None and q is None: 
            return True 

        if p is None or q is None:
            return False 
            
        if p.val != q.val: 
            return False 
        
        
        
        return self.dfs(p.left, q.left) and self.dfs(p.right, q.right)
    
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p,q)