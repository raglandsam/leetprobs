class Solution(object):
    def twoSum(self, nums, tar):
        l = 0
        r = len(nums)-1
        while l < r:
            if nums[l]+nums[r] >tar:
                r-=1
            elif nums[l] + nums[r] < tar:
                l+=1
            else:
                return [l+1,r+1]
