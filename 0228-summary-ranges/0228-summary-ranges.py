class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        l=[]
        start=nums[0]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                if start==nums[i-1]:
                    l.append(str(start))
                else:
                    l.append(str(start) +"->" +str(nums[i-1]))
                start=nums[i]
        if start==nums[-1]:
            l.append(str(start))
        else:
            l.append(str(start) +"->"+str(nums[-1]))
        return l

