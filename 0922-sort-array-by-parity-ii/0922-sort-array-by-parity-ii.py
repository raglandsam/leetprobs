class Solution(object):
    def sortArrayByParityII(self, nums):
        l=len(nums)
       
        e=[n for n in nums if n%2==0]
        o=[n for n in nums if n%2!=0]
        nums=[]
        for i in range(l/2):
            nums.append(e[i])
            nums.append(o[i])

        return nums
