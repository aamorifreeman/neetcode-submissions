import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        heap = []
        for num, freq in seen.items():
            heapq.heappush(heap, (-freq, num))

        
        res = []
        for i in range(k):
            freq, item = heapq.heappop(heap)
            res.append(item)
        
        return res




        

        






        
        

        


        