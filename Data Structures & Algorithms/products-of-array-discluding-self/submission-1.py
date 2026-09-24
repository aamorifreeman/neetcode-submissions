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

        #prefix
        res = []
        prefix = 1

        for i in range(len(nums)):
            res.append(prefix)
            prefix *= nums[i]
        
        #postfix
        postfix = 1

        for i in range(len(nums) -1, -1, -1):
            curr = res[i] * postfix
            res[i] = curr
            
            postfix *= nums[i]
        
        return res

        #final






            



        