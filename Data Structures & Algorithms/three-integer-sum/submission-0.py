class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        n = len(nums)
        targets = [-num for num in nums]
        res = set()
        for i in range(n):
            j, k = i + 1, n - 1
            while j < k:
                if nums[j] + nums[k] < targets[i]:
                    j += 1
                    continue
                elif nums[j] + nums[k] > targets[i]:
                    k -= 1
                    continue
                res.add((nums[i], nums[j], nums[k]))
                j += 1
        
        return list(res)
