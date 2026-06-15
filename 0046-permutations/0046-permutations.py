class Solution(object):
    def permute(self, nums):
        n=len(nums)
        if  n==1:
            return [nums]
        result=[]
        def backtrack(vals,path):
            if len(path)==n and path not in result:
                result.append(path[:])
                return
            for i in nums:
                if i in path:
                    continue
                path.append(i)
                backtrack(i,path)
                path.pop()
        backtrack(nums,[])
        return result


