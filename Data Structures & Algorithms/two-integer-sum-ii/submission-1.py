class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        l = 0
        r = len(nums) - 1

        while l < r:
            calculate sum of nums[l] + nums[r]
            if sum == target:
                return [l, r]
            elif sum greater than target:
                move r pointer left -1
            else: sum less than target
                move l pointer right +1
        return []

        """
        nums = numbers

        l = 0
        r = len(nums) - 1

        while l < r:
            curr_sum = nums[l] + nums[r]
            if curr_sum == target:
                return [l + 1, r + 1]
            elif curr_sum > target:
                r -= 1
            else:
                l += 1
        return []
            


        