from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        d=defaultdict(list)
        for s in strs:
            t=tuple(sorted(s))
            d[t].append(s)
        return d.values()


            

        