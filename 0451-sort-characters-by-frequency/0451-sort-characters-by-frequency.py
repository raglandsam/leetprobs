class Solution(object):
    def frequencySort(self, s):
        heap=[]
        d={}
        st=""
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i,j in d.items():
            heapq.heappush(heap,(-j,i))
        while heap:
            element=heapq.heappop(heap)
            st+=element[1]*(-element[0])
        return st
        


        