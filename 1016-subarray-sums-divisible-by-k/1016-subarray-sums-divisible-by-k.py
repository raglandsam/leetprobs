class Solution(object):
    def subarraysDivByK(self, nums, k):
        s=0
        d={}
        d={0:1}
        c=0
        for i in range(len(nums)):
            s+=nums[i]
            rem=s%k
            rem=(rem+k)%k

            if rem in d:

                c+=d[rem]
                d[rem]+=1
            else:
                d[rem]=1
        return c

            
            




        