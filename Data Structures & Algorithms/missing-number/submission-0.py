class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        prev = nums[0]
        for num in nums[1:]:
            if num - prev > 1:
                break
            prev = num
        return prev + 1