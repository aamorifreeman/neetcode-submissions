import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # seen = {}
        # for num in nums:
        #     if num in seen:
        #         seen[num] += 1
        #     else:
        #         seen[num] = 1
        
        # sorted_by_value = sorted(seen.items(), key=lambda x: x[1], reverse=True)
        # res = []
        # for n, freq in sorted_by_value:
        #     if len(res) < k:
        #         res.append(n)
        
        # return res


        # seen = {}
        # for num in nums:
        #     if num in seen:
        #         seen[num] += 1
        #     else:
        #         seen[num] = 1
        
        # heap = []
        # for num, freq in seen.items():
        #     heapq.heappush(heap, (freq, num))

        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # res = []
        # for freq, num in heap:
        #     res.append(num)
        # return res


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
            freq, num = heapq.heappop(heap)
            res.append(num)
        return res





        

        






        
        

        


        