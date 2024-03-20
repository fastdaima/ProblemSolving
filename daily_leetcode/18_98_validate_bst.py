# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left 
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # each left node: we need to check: left_limit < left_node.value < root_node.value

        # each right node: we need to check: root_node.value < right_node.value < right_limit 
        
        def valid(node, left_limit, right_limit):
            if not node: return True 

            if not (node.val < right_limit and node.val > left_limit): return False

            return valid(node.left,left_limit,node.val) and valid(node.right, node.val, right_limit)

        return valid(root, float('-inf'), float('inf'))
        