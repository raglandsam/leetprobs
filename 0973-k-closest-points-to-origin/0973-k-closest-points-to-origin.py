class Solution(object):
    def kClosest(self, points, k):
        heap=[]
        for i in range(len(points)):
            euc=points[i][0]*points[i][0]+points[i][1]*points[i][1]
            heapq.heappush(heap,(euc,[points[i][0],points[i][1]]))
        return [heapq.heappop(heap)[1] for _ in range(k)]
        




        