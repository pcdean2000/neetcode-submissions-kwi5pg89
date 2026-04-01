class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max, right_max = 0, 0
        
        area = 0
        l, r = 0, n - 1
        while l < r:
            if height[l] < height[r]:
                left_max = max(left_max, height[l])
                area += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                area += right_max - height[r]
                r -= 1
        
        return area