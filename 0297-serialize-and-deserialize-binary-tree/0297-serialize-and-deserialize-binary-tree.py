# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        s=""
        stack=[root]
        while stack:
            root=stack.pop()
            if not root:
                s+="n"+","
            else:
                s+=str(root.val)+","
            if root:
                stack.append(root.right)
                stack.append(root.left)
        return s
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data=data.split(",")
        data=data[0:len(data)-1]
        data=deque(data)
        def helper():
            if not data:
                return None
            val=data.popleft()
            if val=="n":
                return None
            node=TreeNode(int(val))
            node.left=helper()
            node.right=helper()
            return node
        
        return helper()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))