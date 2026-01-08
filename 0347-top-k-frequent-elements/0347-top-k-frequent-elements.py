class Solution(object):
    def topKFrequent(self, nums, k):
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        tup=sorted(d.items(),key=lambda item:item[1],reverse=True)
        return [tup[i][0] for i in range(k)]
        