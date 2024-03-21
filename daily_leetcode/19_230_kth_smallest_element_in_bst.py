
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# doing an preorder traversal to store the node values 
# sorting and sending the k-1 value, since the problem statement is 1 indexed 
# o(n) + o(nLogN)

class Solution:
    def preorder_traversal(self, root: Optional[TreeNode], list_: List) -> List[int]:
        if root: 
            list_.append(root.val)
        if root.left:
            self.preorder_traversal(root.left, list_)
        if root.right:
            self.preorder_traversal(root.right, list_)
        
        return list_

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ordered_list = sorted(self.preorder_traversal(root, []))
        
        return ordered_list[k-1]



