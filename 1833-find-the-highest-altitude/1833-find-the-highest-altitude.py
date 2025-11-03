class Solution(object):
    def largestAltitude(self, gain):
        maxsum=0
        presum=0
        for i in range(len(gain)):
            presum+=gain[i]

            if presum>maxsum:
                maxsum=presum
        return maxsum
        