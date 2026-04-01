class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        n = len(nums)
        targets = [-num for num in nums]
        res = []
        last_num = None
        for i in range(n):
            if nums[i] == last_num:
                continue
            j, k = i + 1, n - 1
            while j < k:
                if nums[j] + nums[k] < targets[i]:
                    j += 1
                    continue
                elif nums[j] + nums[k] > targets[i]:
                    k -= 1
                    continue
                if [nums[i], nums[j], nums[k]] not in res:
                    res.append([nums[i], nums[j], nums[k]])
                j += 1
            last_num = nums[i]
        
        return res
