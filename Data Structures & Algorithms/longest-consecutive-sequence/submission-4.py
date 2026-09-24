class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        """
        nums = [2,20,4,10,3,4,5]
        nums_set = {2, 20, 4, 10, 3, 5}
        
        """
        if len(nums) <= 0:
            return 0


        nums_set = set(nums)
        max_count = 1
        
        for num in nums_set:
            if (num - 1)  not in nums_set: #new sequence
                curr_count = 1
                while(num + curr_count) in nums_set:
                    curr_count += 1
            
                max_count = max(curr_count, max_count)
        
        return max_count
        