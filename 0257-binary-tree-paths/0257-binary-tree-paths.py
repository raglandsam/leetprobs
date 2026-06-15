# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        result=[]
        def findpath(node,path):
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                result.append("->".join(path))
            if node.left:
                findpath(node.left,path)
            if node.right:
                findpath(node.right,path)
            path.pop()
        findpath(root,[])
        return result
        