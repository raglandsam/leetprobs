class Solution(object):
    def combinationSum3(self, k, n):
        arr=[i for i in range(1,10)]
        l=len(arr)
        result=[]
        sum=0
        def find_comb(index,path,sum):
            #BP1, func parameters change
            if sum>n or len(path)>k:
                    return
            if sum==n and len(path)==k:
                result.append(path[:])
                return
            for i in range(index,l):
                path.append(arr[i])
                sum+=arr[i]
                find_comb(i+1,path,sum)
                sum-=path.pop()
        find_comb(0,[],sum)
        return result
