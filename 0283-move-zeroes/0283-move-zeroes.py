class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        if n==1:
            return nums
        c=0
        for i in range(n):
            if nums[i]!=0:
                nums[c]=nums[i]
                c+=1
        for i in range(c, n):
            nums[i]=0
                
        return nums 
        
        