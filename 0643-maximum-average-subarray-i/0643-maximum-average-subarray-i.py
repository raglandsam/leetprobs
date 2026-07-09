class Solution(object):
    def findMaxAverage(self, nums, k):
        curr_sum=float(sum(nums[:k]))
        max_sum=curr_sum/k
        n=len(nums)
    
        for i in range(k, n):
            curr_sum+=nums[i] - nums[i-k]
            curr_avg=curr_sum/k
            max_sum=max(curr_avg,max_sum)
        return max_sum


