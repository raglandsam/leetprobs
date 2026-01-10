class Solution(object):
    def findKthLargest(self, nums, k):
        heap=nums[:k]
        heapq.heapify(heap)
        n=len(nums)
        for i in range(k,n):
            if nums[i]>heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,nums[i])
        return heap[0]
        