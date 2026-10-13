class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        for every num in nums_set:
            if my curr num is the start of a sequence:
                length = 1
                while the sequence continues to exist:
                    length += 1
            max_length = max(max_length, length)
        return max_length
        
        """
        #{2, 20, 4, 10, 3, 5}

        nums_set = set(nums)
        max_length = 0
        length = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                length = 1
                while num + length in nums_set:
                    length += 1
            max_length = max(max_length, length)
        return max_length

        
        