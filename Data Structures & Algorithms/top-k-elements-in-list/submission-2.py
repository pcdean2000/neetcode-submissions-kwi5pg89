class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])
        for key, value in counts.items():
            buckets[value].append(key)

        res = []
        while len(res) < k:
            res.extend(buckets.pop())

        return res