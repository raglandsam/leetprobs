class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        currmax=0
        globmax=-float("inf")
        currmin=0
        globmin=float('inf')
        tot=0
        for num in nums:
            currmax=max(currmax+num, num)
            globmax=max(globmax,currmax)

            currmin=min(currmin+num,num)
            globmin=min(currmin,globmin)
            tot+=num
        if globmax<0:
            return globmax
        return max(globmax,tot-globmin)