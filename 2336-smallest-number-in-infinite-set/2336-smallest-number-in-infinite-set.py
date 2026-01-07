class SmallestInfiniteSet(object):

    def __init__(self):
        self.curr=1
        self.heap=[]
        self.set=set()      

    def popSmallest(self):
        if self.heap:
            smallest=heapq.heappop(self.heap)
            self.set.remove(smallest)
            return smallest 
        self.curr+=1
        return self.curr-1     

    def addBack(self, num):
        if num<self.curr and num not in self.set:
            heapq.heappush(self.heap,num)
            self.set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)