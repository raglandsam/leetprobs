class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(n-2):
            if nums[i]>0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l=i+1
            r=n-1
            while l<r:
                 # or return 
                if nums[i] + nums[l] + nums[r]==0:
                    res.append([nums[i],nums[l],nums[r]])  
                    while l< r and nums[l]==nums[l+1]:
                        l+=1 
                    while r>l and nums[r] ==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif  nums[i] + nums[l] + nums[r] < 0:
                    l+=1
                elif  nums[i] + nums[l] + nums[r] > 0 :
                    r-=1 
        return res       


        