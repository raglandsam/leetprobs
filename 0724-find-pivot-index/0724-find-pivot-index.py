class Solution(object):
    def pivotIndex(self, nums):
        d={}
        d={0:nums[0]}
        n=len(nums)
        for i in range(1,n):
            d[i]=nums[i]+d[i-1]
        for i in range(n):
            left = d[i-1] if i>0 else  0
            right=d[n-1]-d[i]
            if left==right :
                return i
        return -1


        
