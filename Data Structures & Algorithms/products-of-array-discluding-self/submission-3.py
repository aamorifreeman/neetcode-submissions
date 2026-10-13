class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        nums = [1,2,4,6]
        prefix = [1, 1, 2, 8]
        postfix = [48, 24, 6, 1]
        Output = [48,24,12,8]

        prefix = 1
        res = [1, 1, 2, 8]
        for i in range(len(nums)):
            res.append(nums[i] * prefix)
            prefix = nums[i] * prefix

        postfix = 1
        nums = [1,2,4,6]
        prefix = [1, 1, 2, 8]
        res = [48, 24, 12, 8]
        postfix = [48,24,6,1]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix = nums[i] * postfix
        """

        prefix = 1
        res = [prefix]

        for i in range(len(nums) - 1):
            res.append(nums[i] * prefix)
            prefix = nums[i] * prefix
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix = nums[i] * postfix
        
        return res














            



        