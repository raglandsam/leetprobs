class Solution(object):
    def totalCost(self, costs, k, candidates):
        n=len(costs)
        l=0
        r=n-1
        heap1=[]
        heap2=[]
        cost=0
        for _ in range(candidates):
            if l<=r:
                heap1.append(costs[l])
                l+=1
        for _ in range(candidates):
            if r>=l:
                heap2.append(costs[r])
                r-=1
        heapq.heapify(heap1)
        heapq.heapify(heap2)
        for _ in range(k):
            if not heap2 or (heap1 and heap1[0]<=heap2[0]) :
                cost+=heapq.heappop(heap1)
                if l<=r:
                    heapq.heappush(heap1,costs[l])
                    l+=1
            else:
                cost+=heapq.heappop(heap2)
                if r>=l:
                    heapq.heappush(heap2,costs[r])
                    r-=1
        return cost
