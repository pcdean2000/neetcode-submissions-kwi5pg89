class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        counted = {}

        max_length = 0
        for num in nums:
            if num - 1 in seen or num in counted:
                continue
            shift = 1
            while num + shift in seen:
                if num + shift in counted:
                    if shift + counted[num + shift] > max_length:
                        max_length = shift + counted[num + shift]
                    break
                shift += 1
            else:
                counted[num] = shift
            if shift > max_length:
                max_length = shift
        
        return max_length