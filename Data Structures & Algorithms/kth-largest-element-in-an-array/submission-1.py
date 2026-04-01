class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_largest = [-1000] * k
        for i in range(k):
            for j in range(len(k_largest)):
                if k_largest[j] < nums[i]:
                    k_largest.insert(j, nums[i])
                    k_largest.pop(k)
                    break
        for i in range(k, len(nums)):
            for j in range(len(k_largest)):
                if k_largest[j] < nums[i]:
                    k_largest.insert(j, nums[i])
                    k_largest.pop(k)
                    break
        return k_largest[-1]
