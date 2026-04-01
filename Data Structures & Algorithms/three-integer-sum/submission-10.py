class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        n = len(nums)
        res = []
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                current_sum = nums[j] + nums[k]
                if current_sum < -nums[i]:
                    j += 1
                elif current_sum > -nums[i]:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    last_j, last_k = nums[j], nums[k]
                    while j < k and nums[j] == last_j:
                        j += 1
                    while j < k and nums[k] == last_k:
                        k -= 1
        
        return res
