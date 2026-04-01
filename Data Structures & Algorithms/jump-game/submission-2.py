class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        last_index = len(nums) - 1
        for i, num in enumerate(nums):
            if i > max_jump:
                return False
            max_jump = max(max_jump, i + num)
            if max_jump >= last_index:
                return True
        return True