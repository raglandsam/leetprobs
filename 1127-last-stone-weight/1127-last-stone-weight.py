class Solution(object):
    def lastStoneWeight(self, stones):
        while len(stones)>1:
            stones.sort()
            j=stones.pop()
            k=stones.pop()
            if j!=k:
                if j<k:
                    stones.append(k-j)
                elif j>k:
                    stones.append(j-k)
        if stones:
            return stones[0]
        if not stones:
            return 0
