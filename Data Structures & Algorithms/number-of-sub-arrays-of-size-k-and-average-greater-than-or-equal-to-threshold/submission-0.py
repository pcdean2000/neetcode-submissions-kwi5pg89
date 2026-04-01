class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        count = 0
        for r in range(k - 1, len(arr)):
            if r - l >= k:
                l += 1
            if sum(arr[l: r + 1]) / k >= threshold:
                count += 1
        return count