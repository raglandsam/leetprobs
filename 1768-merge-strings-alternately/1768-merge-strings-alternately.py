class Solution(object):
    def mergeAlternately(self, word1, word2):
        o=min(len(word1),len(word2))
        s=''
        l=0
        while l<o:
            s+=word1[l] + word2[l]
            l+=1
        if len(word1)>len(word2):
            s+=word1[l:]
        else:
            s+=word2[l:]
            
        return s


       