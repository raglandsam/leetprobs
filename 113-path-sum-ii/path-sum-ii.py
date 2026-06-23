# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        result=[]
        summ=0
        def find_target(node,path,summ):
            if not root:
                return []
            path.append(node.val)
            summ+=node.val
                   
            if not node.left and not node.right:
                if summ==targetSum:
                    result.append(path[:])
            if node.left:                
                find_target(node.left, path, summ) 
            if node.right :
                find_target(node.right, path, summ)
            summ-=path.pop()
        find_target(root,[],summ)
        return result
            
        