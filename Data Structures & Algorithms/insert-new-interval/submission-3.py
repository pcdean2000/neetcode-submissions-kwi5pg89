class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        # phase 1
        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            else:
                break
            i += 1
        # phase 2
        while i < len(intervals):
            if (intervals[i][0] <= newInterval[0] <= intervals[i][1] or
                intervals[i][0] <= newInterval[1] <= intervals[i][1] or
                newInterval[0] <= intervals[i][0] <= newInterval[1] or
                newInterval[0] <= intervals[i][1] <= newInterval[1]):
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
            else:
                break
            i += 1
        res.append(newInterval)
        # phase 3
        while i < len(intervals):
            res.append(intervals[i])
            i += 1

        return res
