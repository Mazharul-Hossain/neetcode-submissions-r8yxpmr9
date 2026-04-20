import heapq


class MedianFinder:

    def __init__(self):
        self.small_part = [] # max heap
        self.large_part = [] # min heap        

    def addNum(self, num: int) -> None:
        if self.large_part and self.large_part[0] < num:
            heapq.heappush(self.large_part, num)
        
        else:
            heapq.heappush(self.small_part, -num)

        # print(len(self.small_part), len(self.large_part))
        if len(self.small_part) > len(self.large_part) + 1:
            num = -heapq.heappop(self.small_part)
            heapq.heappush(self.large_part, num)
        
        if len(self.large_part) > len(self.small_part):
            num = heapq.heappop(self.large_part)
            heapq.heappush(self.small_part, -num)        
        # print(self.small_part, self.large_part)        

    def findMedian(self) -> float:
        if len(self.small_part) == 0:
            return 0

        if len(self.small_part) == len(self.large_part):
            return (-self.small_part[0] + self.large_part[0]) / 2.0
        
        return -self.small_part[0]