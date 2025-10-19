class Solution(object):
    def reverseVowels(self, s):
        
        l=list(s)
        i=0
        j=len(l)-1
        while i<j:
            if l[i].lower() in ["a","e","i","o","u"] and l[j].lower() in ["a","e","i","o","u"]:
                l[i],l[j]=l[j],l[i]
                i+=1
                j-=1
            elif l[i].lower() in ["a","e","i","o","u"] and l[j].lower() not in ["a","e","i","o","u"]:
                j-=1
            else:
                i+=1
        return "".join(l)
