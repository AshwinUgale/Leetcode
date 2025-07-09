# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxS=float('-inf')
        def dfs(root):
            if not root:
                return 0
            nonlocal maxS
            leftS=max(dfs(root.left),0)
            rightS=max(dfs(root.right),0)
            maxS=max(maxS,leftS+rightS+root.val)
            return root.val+max(leftS,rightS)
        dfs(root)
        return maxS