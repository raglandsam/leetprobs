class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        d={arr1[i]:0 for i in range(len(arr1))}
        for i in range(len(arr1)):
                d[arr1[i]]+=1
        l=[]
        for i in arr2:
            l.extend([i]*d[i])
            del d[i]
        rem=[]
        for key in sorted(d):
            rem.extend([key]*d[key])
        l.extend(rem)
        return l
        #.append(list(set(arr1)-set(arr2)))







