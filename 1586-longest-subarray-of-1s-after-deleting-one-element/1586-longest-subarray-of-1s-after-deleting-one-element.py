class Solution(object):
    def longestSubarray(self, nums):
        if 1 not in nums:
            return 0
        if 0 not in nums:
            return len(nums)-1
        zer=0
        l=0
        r=0
        maxlen=0
        for r in range(len(nums)):
            if nums[r]==0:
                zer+=1
            while zer>1:
                if nums[l]==0:
                    zer-=1
                l+=1
            maxlen=max(maxlen,r-l)

        return maxlen

                

            
            
        