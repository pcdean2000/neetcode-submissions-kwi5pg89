"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.end)
        prev_end = intervals[0].end
        for t in intervals[1:]:
            start, end = t.start, t.end
            if start < prev_end:
                return False
            prev_end = end
        return True
                