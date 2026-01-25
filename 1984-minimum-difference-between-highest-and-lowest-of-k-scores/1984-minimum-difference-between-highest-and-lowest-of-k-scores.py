class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort()
        if len(nums)<=1:
            return nums[0]-nums[0]
        
        window=nums[:k]
        mindiff=window[k-1]-window[0]
        for i in nums[k:]:
            window.pop(0)
            window.append(i)
            mindiff = min(mindiff,window[k-1]-window[0])
        return mindiff

        