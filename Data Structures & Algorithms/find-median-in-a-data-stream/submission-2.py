class MedianFinder:

    def __init__(self):
        self.fhp = [] # max heap
        self.shp = [] # min heap

    def addNum(self, num: int) -> None:
        if self.fhp and (num*-1) >= self.fhp[0]:
            heapq.heappush(self.fhp, num*-1)
        else:
            heapq.heappush(self.shp, num)

        if len(self.fhp) > (len(self.shp) + 1):
            val = -1*heapq.heappop(self.fhp)
            heapq.heappush(self.shp, val)

        if len(self.shp) > (len(self.fhp) + 1):
            val = heapq.heappop(self.shp)
            heapq.heappush(self.fhp, -1*val)


    def findMedian(self) -> float:
        if len(self.fhp) > len(self.shp):
            return -1*self.fhp[0]
        elif len(self.shp) > len(self.fhp):
            return self.shp[0]
        return (-1*self.fhp[0] + self.shp[0])/2
