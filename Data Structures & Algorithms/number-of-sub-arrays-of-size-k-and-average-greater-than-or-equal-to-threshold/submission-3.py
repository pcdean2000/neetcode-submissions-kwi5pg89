class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cur_sum = sum(arr[:k])
        threshold *= k
        count = 1 if cur_sum >= threshold else 0
        for i in range(k, len(arr)):
            cur_sum += (arr[i] - arr[i - k])
            count += cur_sum >= threshold
        return count