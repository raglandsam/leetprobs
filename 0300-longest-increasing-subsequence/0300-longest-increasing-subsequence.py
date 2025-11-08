class Solution(object):
    def lengthOfLIS(self, nums):
        dp=[0]*len(nums)
        dp[0]=1
        for i in range(1,len(nums)):
            maxind=[dp[idx] for idx in range(i) if nums[idx]<nums[i]]
            maxval=max(maxind) if maxind else 0
            dp[i]=max(1,1+maxval)
        return max(dp)