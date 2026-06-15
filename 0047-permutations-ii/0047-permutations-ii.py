class Solution(object):
    def permuteUnique(self, nums):
        n=len(nums)
        if n==1:
            return [nums]
        result=[]
        nums.sort()
        used=[False]*n
        def backtrack(path):
            if len(path)==n:
                result.append(path[:])
                return
            
            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i]==nums[i-1] and not used[i-1]:
                   continue
                used[i]=True
                path.append(nums[i])
                backtrack(path)
                used[i]=False
                path.pop()                
        backtrack([])
        return result

        