class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        local_min = local_max = 1
        global_max = nums[0]
        for num in nums:
            possible_values = [num, num * local_max, num * local_min]
            local_max = max(possible_values)
            local_min = min(possible_values)
            global_max = max(global_max, local_max)

        return global_max
