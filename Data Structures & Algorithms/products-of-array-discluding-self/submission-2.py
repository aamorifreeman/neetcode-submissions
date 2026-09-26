class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        nums = [1,2,4,6]
        prefix = [1, 1, 2, 8]
        postfix = [48, 24, 6, 1]
        Output = [48,24,12,8]
        
        """
        
        #prefix
        res = []
        prefix = 1
        for i in range(len(nums)):
            res.append(prefix)
            prefix *= nums[i]
        
        #postfix
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res









            



        