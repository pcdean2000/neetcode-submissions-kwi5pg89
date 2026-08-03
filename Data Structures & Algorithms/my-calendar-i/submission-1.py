class MyCalendar:
    
    def __init__(self):
        self.reserve = []

    def book(self, startTime: int, endTime: int) -> bool:
        import bisect
        new_book = (startTime, endTime)
        idx = bisect.bisect_left(self.reserve, new_book)
        if idx > 0:
            prev_start, prev_end = self.reserve[idx - 1]
            if prev_end > startTime:
                return False
        if idx < len(self.reserve):
            next_start, next_end = self.reserve[idx]
            if next_start < endTime:
                return False
        bisect.insort(self.reserve, new_book)
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)