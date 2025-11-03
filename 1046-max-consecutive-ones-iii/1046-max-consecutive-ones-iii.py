class Solution(object):
    def longestOnes(self, nums, k):
        l=0
        r=0
        zer=0
        maxlen=0
        while(r<len(nums)):
            if nums[r]==0:
                zer+=1
            while zer>k:
                if nums[l]==0:
                    zer-=1
                l+=1
            maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen

