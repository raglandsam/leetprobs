class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        strs.sort()
        f,l=strs[0],strs[-1]
        pre=""
        p=min(len(f),len(l))
        for i in range(p):
            if f[i]==l[i]:
                pre+=f[i]
            else:
                break
        return pre


        