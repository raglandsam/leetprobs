class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums)<3:
            return False 
        f=float('inf')
        s=float('inf')
        for i in range(len(nums)):
            if nums[i]<=f:
                f=nums[i]
            elif nums[i] <= s:
                s=nums[i]
            elif nums[i] >=s:
                return True
            
        return False 
        