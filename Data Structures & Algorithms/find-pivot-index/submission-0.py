class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        accu_nums = [0] * (length + 2)
        for i in range(length):
            accu_nums[i + 1] = nums[i] + accu_nums[i]

        for i in range(1, len(accu_nums) - 1):
            if accu_nums[i - 1] == accu_nums[length] - accu_nums[i]:
                return i - 1
        else:
            return -1