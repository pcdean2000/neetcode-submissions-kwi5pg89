class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, cur_set):
            if i >= len(nums):
                res.append(cur_set.copy())
                return
            
            cur_set.append(nums[i])
            dfs(i + 1, cur_set)
            
            cur_set.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, cur_set)

        nums.sort()
        res = []
        dfs(0, [])
        return res