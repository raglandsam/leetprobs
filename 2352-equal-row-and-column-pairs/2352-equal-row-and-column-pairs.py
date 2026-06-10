class Solution(object):
    def equalPairs(self, grid):
        pairs=0
        n=len(grid)
        dr={}
        for i in grid:
            if tuple(i) not in dr:
                dr[tuple(i)]=1
            else:
                dr[tuple(i)]+=1
        cols=[tuple(cols) for cols in zip(*grid)]
        dc={}
        for i in cols:
            if i not in dc:
                dc[i]=1
            else:
                dc[i]+=1
        for i in dc:
            if i in dr:
                pairs+=dr[i]*dc[i]
        return pairs