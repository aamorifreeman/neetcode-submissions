class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        nums = numbers
        l = 0
        r = len(nums) - 1 

        while(l < r):
            curr_sum = nums[l] + nums[r]
            if curr_sum > target:
                r -= 1
            elif curr_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []


        