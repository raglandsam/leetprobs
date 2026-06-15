class Solution(object):
    def permuteUnique(self, nums):
        n=len(nums)
        result=[]
        if n==1:
            return [nums]
        count={n:0 for n in nums}
        for i in nums:
            if i in count:
                count[i]+=1
        def backtrack(path):
            if len(path)==n:
                result.append(path[:])
                return 
            for i in count:
                if count[i]>0:
                    path.append(i)
                    count[i]-=1
                    backtrack(path)
                    path.pop()
                    count[i]+=1
        backtrack([])
        return result


        