class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        array=[]
        n=len(nums)
        for i in range(n):
            if i >0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=n-1
            while l<r:
                if nums[l]+nums[i]+nums[r]==0:
                    array.append([nums[l],nums[i],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif nums[l]+nums[i]+nums[r]< 0:
                    l+=1
                else:
                    r-=1
        return array

       


           


        
        