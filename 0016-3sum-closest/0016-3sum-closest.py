class Solution(object):
    def threeSumClosest(self, nums, target):
        s=0
        n=len(nums)
        nums.sort()
        mindiff=float('inf')
        for i in range(n):
            l,r=i+1,n-1
            while l<r:
                if abs((nums[i]+nums[l]+nums[r])-target) < mindiff:
                    s=nums[i]+nums[l]+nums[r]
                    mindiff = abs(s-target)
                elif  nums[i]+nums[l]+nums[r] < target :
                    l+=1
                else :
                    r-=1
        return s

