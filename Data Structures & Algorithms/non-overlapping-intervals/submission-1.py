class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prev_end = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
            if not start < prev_end:
                prev_end = end
                continue
            res += 1
        return res