class Solution(object):
    def maxProduct(self, nums):
        minarr=nums[0]
        maxarr=nums[0]
        res=nums[0]

        for i in range(1,len(nums)):
            curr_prod = nums[i]
            if curr_prod < 0:
                maxarr,minarr=minarr,maxarr

            maxarr=max(curr_prod,curr_prod*maxarr)
            minarr=min(curr_prod,curr_prod*minarr)

            res= max(maxarr,res)
        return res