# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Method 1: Iterative, level order
class Codec:
  
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        stack = [root]
        res = ""
        while (stack):
            cur = stack.pop(0)
            if cur:
                res += str(cur.val)
                stack.append(cur.left)
                stack.append(cur.right)
            res += ','
        return res[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        nums = data.split(',')
        root = TreeNode(nums[0])
        stack = [root]
        i, n = 1, len(nums)
        while i < n:
            cur = stack.pop(0)
            if nums[i]:
                cur.left = TreeNode(nums[i])
                stack.append(cur.left)
            if i < n - 1 and nums[i + 1]:
                cur.right = TreeNode(nums[i + 1])
                stack.append(cur.right)
            i += 2
        return root
#Method 2:Recursive, preorder
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def serial(root):
            if root:
                res[0] += str(root.val) + ','
                serial(root.left)
                serial(root.right)
            else:
                res[0] += ','
        res = [""]
        serial(root)
        return res[0]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dese():
            num = next(nums)
            if not num: 
                return None
            root = TreeNode(int(num))
            root.left = dese()
            root.right = dese()
            return root
        nums = iter(data.split(','))
        return dese()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
