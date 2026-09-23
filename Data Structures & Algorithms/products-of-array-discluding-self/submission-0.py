class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        nums = [1,2,4,6]
        prefix = [1, 1, 2, 8]
        postfix = [48, 24, 6, 1]
        Output = [48,24,12,8]
        
        """
        # first solution
        # prefix = []
        # product = 1
        # for i in range(len(nums)):
        #     curr = nums[i]
        #     prefix.append(product)
        #     product *= curr
        
        # postfix = [0] * len(nums)
        # product2 = 1
        # for i in range(len(nums) - 1, -1, -1):
        #     curr = nums[i]
        #     postfix[i] = product2
        #     product2 *= curr
        
        # output = []
        # for i in range(len(nums)):
        #     curr = prefix[i] * postfix[i]
        #     output.append(curr)
        
        # return output

        output = []
        prefix = 1
        # prefix pass
        for i in range(len(nums)):
            curr = nums[i]
            output.append(prefix)
            prefix *= curr
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            curr = nums[i]
            output[i] *= postfix
            postfix *= curr
        
        return output



            



        