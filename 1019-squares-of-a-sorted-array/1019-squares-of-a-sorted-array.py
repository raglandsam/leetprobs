class Solution(object):
    def sortedSquares(self, nums):
        return sorted([i*i for i in nums])