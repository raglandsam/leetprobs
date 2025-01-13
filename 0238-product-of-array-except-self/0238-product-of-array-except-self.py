class Solution(object):
    def productExceptSelf(self, nums):
        l=[0] * len(nums)
        lp=[0]*len(nums)
        lp[0]=1
        for i in range(1,len(nums)):
            lp[i]=lp[i-1]*nums[i-1]
        rp=1
        for i in range(len(nums)-1,-1,-1):
            l[i]=lp[i]*rp
            rp*=nums[i]
        return l

            

        
