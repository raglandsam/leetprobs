class Solution(object):
    def maxVowels(self, s, k):
        win =0
        v="aeiou"
        curr=sum(c.lower() in v for c in s[:k])
        win=curr
        for i in range(k,len(s)):
            if s[i].lower()  in v:
                curr+=1
            if s[i-k].lower() in v:
                curr-=1            
            win=max(win, curr)            
        return win

            