import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        
        min_heap = []

        for n, f in counter.items():
            heapq.heappush(min_heap, (f, n))
            while len(min_heap) > k:
                _ = heapq.heappop(min_heap)
        
        answer = []
        for f, n in min_heap:
            answer.append(n)
        
        return answer
