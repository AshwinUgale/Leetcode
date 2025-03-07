# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Recursive
        # arr=[]
        # def recursive(root):
        #     if not root:
        #         return 
        #     recursive(root.left)
        #     arr.append(root.val)
        #     recursive(root.right)
        # recursive(root)
        # return arr

        #Iterative
        arr=[]
        stack =[]
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            arr.append(cur.val)
            cur = cur.right
        return arr

            

