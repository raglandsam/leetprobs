class Solution(object):
    def uniqueOccurrences(self, arr):
        d={}
        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]]=1
            else:
                d[arr[i]]+=1
        return len(set(d.values()))==len(d.values())

        