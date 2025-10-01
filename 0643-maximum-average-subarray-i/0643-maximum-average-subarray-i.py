class Solution(object):
    def findMaxAverage(self, nums, k):
        summ = sum(nums[:k])
        max_sum =summ
        for i in range(k,len(nums)):
            summ+=nums[i]
            summ-=nums[i-k]
            max_sum=max(max_sum , summ)

        return float(max_sum)/float(k)