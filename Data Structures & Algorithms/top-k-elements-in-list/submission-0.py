import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]]+=1
            else:
               seen[nums[i]]=1
        
        heap = []
        for num, freq in seen.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []

        for freq, num in heap:
            ans.append(num)
        return ans

        


        