class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d={}
        for i in range(len(nums)):
            if nums[i] in d and (i-d[nums[i]] <= k) :
                return True
            d[nums[i]]=i
        return False 

"""

        i=0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i==j:
                    continue
                elif nums[i]==nums[j] and abs(i-j)<=k:
                    return True 
        return False  """       