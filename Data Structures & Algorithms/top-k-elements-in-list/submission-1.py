class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        max_freq = 0
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > max_freq:
                max_freq = counts[num]
        
        buckets = []
        for i in range(max_freq + 1):
            buckets.append([])
        for key, value in counts.items():
            buckets[value].append(key)

        res = []
        while len(res) < k:
            res.extend(buckets.pop())

        return res