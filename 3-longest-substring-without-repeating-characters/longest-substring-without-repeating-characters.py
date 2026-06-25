class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        d={}
        n=len(s)
        if n==1:
            return 1
        maxlen=0
        l=0
        for i in range(n):
            if s[i] in d and d[s[i]]>=l:
                l=d[s[i]]+1
            d[s[i]]=i
            maxlen=max(maxlen,i-l+1)
        return maxlen
       

        