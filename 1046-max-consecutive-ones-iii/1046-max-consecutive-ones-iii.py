class Solution(object):
    def longestOnes(self, nums, k):
        l=0
        r=0
        zer=0
        maxlen=0
        for i in range(len(nums)):
            if nums[i]==0:
                zer+=1
            if zer>k:
                if nums[l]==0:
                    zer-=1
                l+=1
            maxlen=max(maxlen,i-l+1)
        return maxlen

