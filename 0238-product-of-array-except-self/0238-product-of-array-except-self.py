class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        pre=[1]*len(nums)
        suf=[1]*len(nums)
        pre[0]=1
        for i in range(1,n):
            pre[i]=pre[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            suf[i]=suf[i+1]*nums[i+1]
        return [o*p for o,p in zip(pre,suf)]

            

        
