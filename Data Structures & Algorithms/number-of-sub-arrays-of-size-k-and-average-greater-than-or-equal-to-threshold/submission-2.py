class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        cur_sum = sum(arr[:k])
        threshold *= k
        if cur_sum >= threshold:
            count += 1
        for i in range(k, len(arr)):
            cur_sum += (arr[i] - arr[i - k])
            if cur_sum >= threshold:
                count += 1
        return count