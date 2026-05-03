class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for el in nums:
            dct[el] = 1 + dct.get(el, 0)

        heap = []
        for key, val in dct.items():
            heapq.heappush(heap, (val, key))
            if len(heap)>k:
                heapq.heappop(heap)

        return [el[1] for el in heap]