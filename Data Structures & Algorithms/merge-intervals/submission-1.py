class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for i in range(len(intervals)):
            if i < (len(intervals) - 1) and intervals[i][1] >= intervals[i + 1][0]:
                intervals[i + 1][0] = min(intervals[i][0], intervals[i + 1][0])
                intervals[i + 1][1] = max(intervals[i][1], intervals[i + 1][1])
            else:
                res.append(intervals[i])
        return res