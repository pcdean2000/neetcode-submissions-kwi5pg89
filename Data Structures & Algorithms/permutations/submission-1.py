class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, idx):
            if idx == len(nums):
                res.append(nums[:])
                return
            
            for i in range(idx, len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                backtrack(nums, idx + 1)
                nums[i], nums[idx] = nums[idx], nums[i]
        
        res = []
        backtrack(nums, 0)
        return res
