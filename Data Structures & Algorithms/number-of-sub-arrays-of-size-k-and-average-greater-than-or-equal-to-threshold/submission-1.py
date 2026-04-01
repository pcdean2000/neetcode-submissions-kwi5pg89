class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        count = 0
        avg = sum(arr[:k])
        threshold *= k
        for r in range(k - 1, len(arr)):
            if r - l >= k:
                avg += (arr[r] - arr[l])
                l += 1
            if avg >= threshold:
                count += 1
        return count