# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder_t(self, root, out = []):
        if root:
            out.append(root.val)
            self.preorder_t(root.left, out)
            self.preorder_t(root.right, out)
        else:
            out.append(None)
        return out 

    
    def check_subroot(self ,root, subRoot):
        preorder_t = self.preorder_t(root, [])
        print(preorder_t, subRoot)
        if preorder_t == subRoot: 
            print('its true')
            return True 

        if root.left: 
            if self.check_subroot(root.left, subRoot): return True
        if root.right:
            if self.check_subroot(root.right, subRoot): return True

        return False



    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subRoot = self.preorder_t(subRoot, [])
        return self.check_subroot(root, subRoot)
       

# using strings very nice solution 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def to_string(root):
            if root == None: return "$"

            return " ->" + str(root.val) + "#" + to_string(root.left) + to_string(root.right)
        
        print(to_string(root))
        print(to_string(subRoot))

        return to_string(subRoot) in to_string(root)

        