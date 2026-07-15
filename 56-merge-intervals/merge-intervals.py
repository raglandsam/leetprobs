class Solution(object):
    def merge(self, intervals):
        if len(intervals)==0:
            return []
        if len(intervals)==1:
            return intervals
        intervals.sort()
        
        merged=[intervals[0]]
        for inter in intervals[1:]:
            if inter[0] <= merged[-1][1] :
                if inter[1] >  merged[-1][1]:
                    merged[-1][1] = inter[1]
                    
            elif inter[0] > merged[-1][1] :
                
                merged.append(inter)
        return merged
            