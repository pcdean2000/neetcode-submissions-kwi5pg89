class MyCalendar:
    
    def __init__(self):
        self.reserve = []

    def book(self, startTime: int, endTime: int) -> bool:
        for existingStart, existingEnd in self.reserve:
            if startTime < existingEnd and endTime > existingStart:
                return False
        self.reserve.append([startTime, endTime])
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)