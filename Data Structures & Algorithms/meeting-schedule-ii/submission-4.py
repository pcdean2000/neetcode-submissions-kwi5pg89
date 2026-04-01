"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        heap_room = []
        for interval in intervals:
            if heap_room and not interval.start < heap_room[0]:
                heapq.heappop(heap_room)
            heapq.heappush(heap_room, interval.end)
        return len(heap_room)
