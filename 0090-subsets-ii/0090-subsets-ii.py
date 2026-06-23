class Solution(object):
    def subsetsWithDup(self, nums):
        results =[]
        n=len(nums)
        nums.sort()
        if n==1:
            return [[],nums]
        def backtrack(index,path):
            if path not in results:
                results.append(path[:])
            #bp1:try n-1
            for i in range(index,n):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        backtrack(0,[])
        return results

        