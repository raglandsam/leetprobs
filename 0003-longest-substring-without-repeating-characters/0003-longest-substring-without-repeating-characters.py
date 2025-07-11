class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        else:
            d={}
            max_l=0
            l=0
            for i in range(len(s)):
                if s[i] in d and d[s[i]]>=l:
                    l=d[s[i]]+1
                d[s[i]]=i

                max_l=max(max_l,i-l+1)
        return max_l
