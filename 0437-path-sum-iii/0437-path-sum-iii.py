# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        if not root :
            return 0
        self.count=0
        d={0:1}
        def dfs(node,curr_sum):
            if not node:
                return
            curr_sum+=node.val
            old_sum=curr_sum - targetSum
            if old_sum in d:
                self.count+=d[old_sum]
            if curr_sum not in d:
                d[curr_sum]=1
            else:
                d[curr_sum]+=1
            dfs(node.left,curr_sum)
            dfs(node.right,curr_sum)

            d[curr_sum]-=1
        dfs(root,0)
        return self.count

            