class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        n = len(nums)
        targets = [-num for num in nums]
        res = []
        last_i = None
        for i in range(n):
            if nums[i] == last_i:
                continue
            j, k = i + 1, n - 1
            last_j, last_k = None, None
            while j < k:
                if nums[j] + nums[k] < targets[i]:
                    j += 1
                    continue
                elif nums[j] + nums[k] > targets[i]:
                    k -= 1
                    continue
                if nums[j] == last_j and nums[k] == last_k:
                    j += 1
                    continue
                res.append([nums[i], nums[j], nums[k]])
                last_j, last_k = nums[j], nums[k]
                j += 1
            last_i = nums[i]
        
        return res
