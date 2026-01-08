class Solution(object):
    def maxScore(self, nums1, nums2, k):
        n=len(nums2)
        nums1heap=[]
        pairs=sorted(zip(nums2,nums1),reverse=True)
        score=0
        summ=0
        for val2,val1 in pairs:
            heapq.heappush(nums1heap,val1)
            summ+=val1
            if len(nums1heap)>k:
                summ-=heapq.heappop(nums1heap)
            if len(nums1heap)==k:
                score=max(score,summ*val2)
        return score
                




            
        

        