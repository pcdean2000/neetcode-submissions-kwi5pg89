"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        heap_room = [(intervals[0].end, intervals[0].start)]
        heapq.heapify(heap_room)
        for interval in intervals[1:]:
            if interval.start < heap_room[0][0]:
                heapq.heappush(heap_room, (interval.end, interval.start))
                continue
            heapq.heappop(heap_room)
            heapq.heappush(heap_room, (interval.end, interval.start))
        return len(heap_room)
