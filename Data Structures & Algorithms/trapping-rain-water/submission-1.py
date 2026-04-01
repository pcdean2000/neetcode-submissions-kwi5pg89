class Solution:
    def trap(self, height: List[int]) -> int:

        def pass_one(direction : bool):
            cur_area = 0
            if direction is True:
                l, end, interval = 0, len(height), 1
            else:
                l, end, interval = len(height) - 1, -1, -1
            for r in range(l, end, interval):
                if height[l] > height[r]:
                    continue
                # 使用 height[l] 把 l ~ r 的空間填平
                cur_height = height[l]
                while l * interval < r * interval:
                    cur_area += cur_height - height[l]
                    height[l] = cur_height
                    l += interval
            return cur_area

        # 1-pass (left-to-right)
        area = pass_one(True)
        # 2-pass (right-to-left)
        area += pass_one(False)

        return area