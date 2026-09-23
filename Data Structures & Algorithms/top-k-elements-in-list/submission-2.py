import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (-freq, num))
        
        res = []
        for i in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)
        return res

        
        

        


        