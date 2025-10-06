class Solution(object):
    def minSubArrayLen(self, target, nums):
        i=0
        n=len(nums)
        tot=0
        minlen=float('inf')
        for j in range(n):
            tot+=nums[j]

            while tot >= target :
                minlen=min(minlen,j-i+1)
                tot-=nums[i]
                i+=1
        return 0 if minlen==float('inf') else minlen




