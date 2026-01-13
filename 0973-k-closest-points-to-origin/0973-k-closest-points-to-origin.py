class Solution(object):
    def kClosest(self, points, k):
        arr=[]
        l=[]
        for i in points:
            euc=(i[0]*i[0]+i[1]*i[1])
            arr.append([euc,[i[0],i[1]]])
        arr=sorted(arr , key= lambda x:x[0])
        return [arr[i][1] for i in range(k)]



        