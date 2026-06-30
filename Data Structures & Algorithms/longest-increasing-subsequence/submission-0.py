class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        def dfs(i, prev):
            if i == n:
                return 0
            if (i, prev) in dp:
                return dp[(i, prev)]
            pos = []
            if nums[i] > prev:
                pos.append(dfs(i + 1, nums[i]) + 1)
            pos.append(dfs(i + 1, prev))
            dp[(i, prev)] = max(pos)
            return max(pos)

        return dfs(0, -float('inf'))