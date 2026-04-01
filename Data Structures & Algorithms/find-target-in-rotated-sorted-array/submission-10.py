class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 先找到 cut
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) >> 1
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        cut = l
        # 再找 target 位置
        l, r = 0, len(nums) - 1
        if nums[cut] <= target <= nums[r]:
            l = cut
        else:
            r = cut - 1
        while l <= r:
            m = (l + r) >> 1
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return -1