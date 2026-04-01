class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        counted = {}

        max_length = 0
        for num in nums:
            if num - 1 in seen:
                continue
            shift = 1
            while num + shift in seen:
                if num + shift in counted:
                    if shift > max_length:
                        max_length = shift
                    break
                shift += 1
            counted[num] = shift
            if shift > max_length:
                max_length = shift
        
        return max_length