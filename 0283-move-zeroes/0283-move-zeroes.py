class Solution(object):
    def moveZeroes(self, nums):
        nonzeros=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[nonzeros]=nums[i]
                nonzeros+=1
        for i in range(nonzeros,len(nums)):
            nums[i]=0