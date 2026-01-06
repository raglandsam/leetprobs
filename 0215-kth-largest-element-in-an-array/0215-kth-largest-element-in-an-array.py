class Solution(object):
    def findKthLargest(self, nums, k):
        n=len(nums)        
        def heapify(n,idx):
            
            while True :
                largest=idx
                l=2*idx+1
                r=2*idx+2
                if l<n and nums[l]>nums[largest]:
                    largest=l
                if r<n and nums[r]>nums[largest]:
                    largest=r
                if largest==idx:
                    break
                nums[idx],nums[largest]=nums[largest],nums[idx]
                idx=largest
        for i in range((n-1)//2,-1,-1):
            heapify(n,i)
        for _ in range(k-1):
            nums[0],nums[n-1]=nums[n-1],nums[0]
            n-=1
            heapify(n,0)
        return nums[0]
