class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        while i < len(intervals):
            if (intervals[i][0] <= newInterval[0] <= intervals[i][1] or
                intervals[i][0] <= newInterval[1] <= intervals[i][1] or
                newInterval[0] <= intervals[i][0] <= newInterval[1] or
                newInterval[0] <= intervals[i][1] <= newInterval[1]):
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
                intervals.pop(i)
                continue
            i += 1
        i = 0
        while i < len(intervals):
            if newInterval[1] < intervals[i][0]:
                break
            i += 1
        intervals.insert(i, newInterval)
        return intervals
            