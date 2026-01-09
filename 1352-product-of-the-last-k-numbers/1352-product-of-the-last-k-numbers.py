class ProductOfNumbers(object):
    def __init__(self):
        self.pref=[1]
        self.idx=0
    def add(self, num): 
        if self.pref and num>0:
            self.idx+=1
            self.pref.append(self.pref[-1]*num)
        elif num <=0:
            self.pref=[1]
            self.idx=0

    def getProduct(self, k):
        if self.idx<k:
            return 0
        else:
            return self.pref[self.idx]/self.pref[self.idx-k]     
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
