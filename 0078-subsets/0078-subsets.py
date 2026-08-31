class Solution(object):
    def subsets(self, nums):
        res=[]
        def recurse(index,path):
            res.append(path[:])
            for i in range(index,len(nums)):
                path.append(nums[i])
                recurse(i+1, path)
                path.pop()
        recurse(0,[])
        return res