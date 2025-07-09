# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashs={}
        for r in range(len(inorder)):
            hashs[inorder[r]]=r
        curR=0
        def helper(leftI,rightI):
            if leftI>rightI:
                return None
            nonlocal curR
            rootVal= preorder[curR]
            curR+=1
            root=TreeNode(rootVal)

            index = hashs[rootVal]
            root.left=helper(leftI,index-1)
            root.right=helper(index+1,rightI)

            return root
        return helper(0,len(inorder)-1)
       
            
