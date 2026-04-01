class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = {0: 1}
        prefix_sum = 0
        result = 0
        for num in nums:
            prefix_sum += num
            target = prefix_sum - k
            if target in counts:
                result += counts[target]
            counts[prefix_sum] = counts.get(prefix_sum, 0) + 1
        return result