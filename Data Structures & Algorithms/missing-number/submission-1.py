class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_map = {i: i for i in range(len(nums) + 1)}
        for num in nums:
            num_map[num] ^= num
        for num in num_map.values():
            if num:
                return num
        return 0
