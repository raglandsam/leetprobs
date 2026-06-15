class Solution(object):
    def permute(self, nums):
        n=len(nums)
        if  n==1:
            return [nums]
        result=[]
        def backtrack(path):
            if len(path)==n:
                result.append(path[:])
                return
            for i in nums:
                if i in path:
                    continue
                path.append(i)
                backtrack(path)
                path.pop()
        backtrack([])
        return result


