class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        pref_prod=[1]*n
        suff_prod=[1]*n
        pref_prod[0]=nums[0]
        suff_prod[-1]=nums[-1]
        for i in range(1,n):
            pref_prod[i]=nums[i]*pref_prod[i-1]
        for i in range(n-2,-1,-1):
            suff_prod[i] = nums[i] * suff_prod[i+1] #i+1 or i
        nums[0]=suff_prod[1]
        nums[-1]=pref_prod[n-2]
        for i in range(1,n-1):
            nums[i]=pref_prod[i-1]*suff_prod[i+1]
        return nums
        
        