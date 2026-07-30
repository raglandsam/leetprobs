class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d={nums[i]: 0 for i in range(len(nums))}
        for i in nums:
            d[i]+=1
              
        d=dict(sorted(d.items(), key=lambda item:(item[1],-item[0])))
        l=[]
        for k,e in d.items():
            l.extend([k]*e)
        return l
