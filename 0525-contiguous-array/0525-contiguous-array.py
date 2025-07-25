class Solution(object):
    def findMaxLength(self, nums):
        l=[-1 if i==0 else 1 for i in nums]
        d={0:-1} 
        s=0 
        max_len=0 
        for i in range(len(l)): 
            s+=l[i] 
            if s not in d: 
                d[s]=i 
            else : 
                max_len=max(max_len,i-d[s]) 
        return max_len 
        