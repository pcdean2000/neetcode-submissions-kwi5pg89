class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        max_length = 0
        for num in seen:
            if num - 1 in seen:
                continue
            shift = 1
            while num + shift in seen:
                shift += 1
            if shift > max_length:
                max_length = shift
        
        return max_length