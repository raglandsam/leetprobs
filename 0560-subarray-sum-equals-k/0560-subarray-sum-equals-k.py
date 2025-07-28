class Solution(object):
    def subarraySum(self, nums, k):
        c=0
        d={}
        d={0:1}
        curr_sum=0
        for i in range(0,len(nums)):
            curr_sum+=nums[i]
            if (curr_sum-k) in d:
                    c+=d[curr_sum-k]
            if curr_sum in d:
                d[curr_sum]+=1
            else:
                d[curr_sum]=1
            
        return c


                
       

       