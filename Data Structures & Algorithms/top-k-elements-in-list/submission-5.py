import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        sorted_by_value = sorted(seen.items(), key=lambda x: x[1], reverse=True)
        res = []
        for n, freq in sorted_by_value:
            if len(res) < k:
                res.append(n)
            else:
                break
        
        return res





        

        






        
        

        


        