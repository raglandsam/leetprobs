class Solution(object):
    def closeStrings(self, word1, word2):
        if len(word1)!=len(word2):
            return False
        if word1==word2:
            return True
        def freq(word):
            d={}
            for i in word:
                if i not in d:
                    d[i]=1
                else:
                    d[i]+=1
            return d
        d1=freq(word1)
        d2=freq(word2)
        if set(d1.keys())!=set(d2.keys()):
            return False
        if sorted(d1.values())!=sorted(d2.values()):
            return False
        return True
        