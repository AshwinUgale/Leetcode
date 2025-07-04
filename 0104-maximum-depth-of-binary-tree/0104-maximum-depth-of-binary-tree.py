# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Recursive
        # if not root:
        #     return 0
        # return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

        #iterative
        if not root:
            return 0
        stack = [root]
        depth = [1]
        maxDepth=0
        while stack:
            r,d=stack.pop(),depth.pop()
            if r:
                maxDepth=max(maxDepth,d)
                stack.append(r.right)
                depth.append(d+1)
                stack.append(r.left)
                depth.append(d+1)
            
        return maxDepth

