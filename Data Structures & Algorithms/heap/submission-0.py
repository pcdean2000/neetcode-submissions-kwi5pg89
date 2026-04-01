class MinHeap:
    
    def __init__(self):
        self.heapQueue = [0]

    def push(self, val: int) -> None:
        self.heapQueue.append(val)
        self.perculate()

    def pop(self) -> int:
        if not self.check():
            return -1
        self.heapQueue[1], self.heapQueue[-1] = self.heapQueue[-1], self.heapQueue[1]
        res = self.heapQueue.pop()
        self.perculate()

        return res

    def top(self) -> int:
        if not self.check():
            return -1
        return self.heapQueue[1]

    def heapify(self, nums: List[int]) -> None:
        self.heapQueue = [0]
        self.heapQueue.extend(nums)
        self.perculate()
    
    def perculate(self) -> None:
        cur_index = (len(self.heapQueue) - 1) // 2
        
        while cur_index > 0:
            
            if 2 * cur_index + 1 < len(self.heapQueue) and self.heapQueue[2 * cur_index + 1] < self.heapQueue[cur_index] and self.heapQueue[2 * cur_index + 1] < self.heapQueue[2 * cur_index]:
                self.heapQueue[cur_index], self.heapQueue[2 * cur_index + 1] = self.heapQueue[2 * cur_index + 1], self.heapQueue[cur_index]
            elif 2 * cur_index < len(self.heapQueue) and self.heapQueue[2 * cur_index] < self.heapQueue[cur_index]:
                self.heapQueue[cur_index], self.heapQueue[2 * cur_index] = self.heapQueue[2 * cur_index], self.heapQueue[cur_index]
            
            cur_index -= 1
    
    def check(self):
        return len(self.heapQueue) > 1
