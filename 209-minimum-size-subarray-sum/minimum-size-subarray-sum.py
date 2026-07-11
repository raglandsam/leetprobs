class Solution(object):
    def minSubArrayLen(self, target, nums):
        if target in nums:
            return 1
        n=len(nums)
        minlen=float('inf')
        l=0
        curr_sum=0
        for r in range(n):
            curr_sum+=nums[r]
            while curr_sum >= target:
                minlen=min(minlen,r-l+1)
                l+=1
                curr_sum-=nums[l-1]
        return minlen if minlen!=float('inf') else 0


