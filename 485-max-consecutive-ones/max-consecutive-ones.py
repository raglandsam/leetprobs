class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        summ=sum(nums)
        if summ <=1:
            return summ
        count=0
        maxones=0
        for i in nums:
            if i ==1:
                count+=1
                maxones=max(maxones,count)
            else:
                count=0
        
        return maxones


        

        