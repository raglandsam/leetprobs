class Solution(object):
    def numberOfSubstrings(self, s):
        n=len(s)
        c=0
        d={'a':-1,'b':-1,'c':-1}
        n=len(s)
    
        for i in range(n):
            d[s[i]]=i
            if d['a']!=-1 and d['b']!=-1 and d['c']!=-1:
                min_idx=min(d['a'],d['b'],d['c'])
                c+=min_idx+1
           

        return c

        