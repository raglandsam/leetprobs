class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if len(nums)<=1:
            return nums
        d={}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        tup=sorted(d.items(),key=lambda item:-item[1])
        return [item[0] for item in tup[:k]]