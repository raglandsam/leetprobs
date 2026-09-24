class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        maxlen=1
        start=0
        def expand_from(l,r):
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                l-=1
                r+=1
            return l+1,r-1
        for i in range(len(s)-1):
            l1,r1=expand_from(i,i)
            if (r1-l1+1)>maxlen:
                start=l1
                maxlen=r1-l1+1
            l2,r2=expand_from(i,i+1)
            if (r2-l2+1) > maxlen:
                start=l2
                maxlen=r2-l2+1
        return s[start:start+maxlen]