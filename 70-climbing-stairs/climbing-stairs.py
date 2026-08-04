class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        prev=0
        curr=1
        for _ in range(n):
            prev, curr = curr, prev +curr
        return curr
        