class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        """
        nums = [2,20,4,10,3,4,5]
        nums_set = {2, 20, 4, 10, 3, 5}

        convert nums to a set
        loop though nums_set
            if num - 1 not in nums_set: start of sequence
                while num + i in set
                    count += 1
                    nums_set.remove(num + i)
                max_len = max(max_len, count)
        return max_len
        
        """

        nums_set = set(nums)
        max_len = 0
        for num in nums_set:
            if (num - 1) not in nums_set: #start of a sequence
                count = 1
                while (num + count) in nums_set:
                    count += 1
                    #nums_set.remove(num + count)
                max_len = max(max_len, count)
        return max_len
        
        