class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(nums):
            prev2 = prev1 = 0
            for num in nums:
                current = max(prev2 + num, prev1)
                prev2 = prev1
                prev1 = current
            return prev1

        return max(helper(nums[:-1]), helper(nums[1:]))