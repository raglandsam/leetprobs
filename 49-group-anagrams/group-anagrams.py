class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d={}
        for word in strs:
            tup=tuple(sorted(word))
            if tup in d:
                d[tup].append(word)
            else:
                d[tup]=[word]
        return list(d.values())