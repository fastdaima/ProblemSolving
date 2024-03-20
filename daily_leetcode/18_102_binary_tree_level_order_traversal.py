# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. solved using recursion 
# passed the output dictionary between states
# and at the end returned the value 

class Solution:

    def lot(self, root, level, out):
        if root:
            if level in out: 
                out[level].append(root.val)
            else:
                out[level] = [root.val]
        
            if root.left: self.lot(root.left, level+1, out)
            if root.right: self.lot(root.right, level+1, out)

        return out


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = self.lot(root, 0, {})
        print(list(out.values()))
        return list(out.values()) if out else []


# 2. solved using queue 
# used deque for pop left concept and O(1)
# starts with root 
# iterating the deque for the current size, because we will poping leftmost node
# if root and then appends value to level
# if root.left and root.right appends value to the deque 
# at the end of each iteration of deque: appends level list to final list  


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []

        queue = deque([root])

        while queue: 
            size = len(queue)
            level = []
            for i in range(size):
                node = queue.popleft()

                if node:
                    level.append(node.val)

                    if node.left: 
                        queue.append(node.left)
                    
                    if node.right: 
                        queue.append(node.right)
            if level: result.append(level)
        
        return result        