class Solution(object):
    def maxSubArray(self, nums):
        maxsum= nums[0]
        currsum= nums[0]
        for num in nums[1:]:
            currsum = max(currsum+num, num)
            maxsum = max(maxsum, currsum)
        return maxsum