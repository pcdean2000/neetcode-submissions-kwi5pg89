class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 先找到 cut
        l, r = 0, len(nums) - 1
        if nums[l] > nums[r]:
            while l < r:
                m = (l + r) >> 1
                if nums[m] > nums[l]:
                    l = m
                else:
                    r = m
        cut = r
        # 再找 target 位置
        if target >= nums[0]:
            l, r = 0, cut
        else:
            l, r = cut + 1, len(nums) - 1
        while l < r:
            m = (l + r) >> 1
            if target > nums[m]:
                l = m + 1
            else:
                r = m
        return r if target == nums[r] else -1