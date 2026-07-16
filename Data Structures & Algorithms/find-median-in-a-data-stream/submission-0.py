import bisect

class MedianFinder:

    def __init__(self):
        self.data = []
        self.length = 0

    def addNum(self, num: int) -> None:
        bisect.insort(self.data, num)
        self.length += 1

    def findMedian(self) -> float:
        if self.length % 2 == 0:
            median = (self.data[self.length // 2] + self.data[self.length // 2 - 1]) / 2
        else:
            median = self.data[self.length // 2]
        return median
        
        