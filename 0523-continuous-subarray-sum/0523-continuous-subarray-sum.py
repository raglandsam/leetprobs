class Solution(object):
    def checkSubarraySum(self, nums, k):        
        d={0:-1}
        cu_sum=0
        for i in range (len(nums)):
            cu_sum+=nums[i]
            rem=cu_sum%k
            rem=(rem+k)%k
            if rem in d:
                if i-d[rem]>=2:
                    return True 
            else:
                d[rem]=i
        return False