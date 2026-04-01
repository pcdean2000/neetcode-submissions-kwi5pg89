class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left_prod, right_prod = [1] * (length + 1), [1] * (length + 1)
        for i in range(length):
            left_prod[i + 1] = left_prod[i] * nums[i]
        for i in range(length - 1, -1, -1):
            right_prod[i] = right_prod[i + 1] * nums[i]
        return [left_prod[i] * right_prod[i + 1] for i in range(length)]
