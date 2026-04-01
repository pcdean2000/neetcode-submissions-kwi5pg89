class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        longest = 0

        for num in nums:
            if mp[num] > 0:
                continue
            mp[num] = mp[num - 1] + mp[num + 1] + 1
            mp[num - mp[num - 1]] = mp[num]
            mp[num + mp[num + 1]] = mp[num]
            longest = max(longest, mp[num])
        
        return longest
