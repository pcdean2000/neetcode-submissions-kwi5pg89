class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        n = len(nums)
        targets = [-num for num in nums]
        res = []
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                if nums[j] + nums[k] < targets[i]:
                    j += 1
                    continue
                elif nums[j] + nums[k] > targets[i]:
                    k -= 1
                    continue
                res.append([nums[i], nums[j], nums[k]])
                last_j, last_k = nums[j], nums[k]
                while j < k and nums[j] == last_j:
                    j += 1
                while j < k and nums[k] == last_k:
                    k -= 1
        
        return res
