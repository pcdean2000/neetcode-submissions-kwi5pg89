class DSU:
    def __init__(self, n: int) -> None:
        self.components = n
        self.parent = {i: i for i in range(n)}
        self.size = {i: 1 for i in range(n)}
    
    def find(self, node: int) -> int:
        par = self.parent[node]
        if par != node:
            self.parent[node] = self.find(par)
        return self.parent[node]
    
    def union(self, u: int, v: int) -> bool:
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return False
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.size[pu] += self.size[pv]
        self.components -= 1
        return True

    def get_components(self) -> int:
        return self.components

class MinHeap:
    def __init__(self) -> None:
        self.arr = [[]]

    def push(self, val: List) -> None:
        # percolate up
        self.arr.append(val)
        self.percolate_up()
    
    def pop(self) -> List:
        # percolate down
        if len(self.arr) <= 1:
            return []
        if len(self.arr) == 2:
            return self.arr.pop()
        val = self.top()
        self.arr[1] = self.arr.pop()
        i = 1
        
        self.percolate_down(i)

        return val
    
    def heapify(self, nums: List[List[int]]) -> None:
        # percolate down
        self.arr.extend(nums)
        for i in range((len(self.arr) - 1) // 2, 0, -1):
            self.percolate_down(i)
    
    def top(self) -> List:
        if len(self.arr) <= 1:
            return []
        return self.arr[1]

    def percolate_up(self) -> None:
        i = len(self.arr) - 1
        while i > 1 and self.arr[i][0] < self.arr[i // 2][0]:
            self.swap(i, i // 2)
            i //= 2

    def percolate_down(self, i) -> None:
        while i * 2 < len(self.arr):
            child = i * 2
            if child + 1 < len(self.arr) and self.arr[child + 1][0] < self.arr[child][0]:
                child += 1
            
            if self.arr[i][0] > self.arr[child][0]:
                self.swap(i, child)
                i = child
            else:
                break

    def swap(self, i1, i2) -> None:
        self.arr[i1], self.arr[i2] = self.arr[i2], self.arr[i1]

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        edge_heapq = MinHeap()
        edge_heapq.heapify([[w, u, v] for u, v, w in edges])

        dsu = DSU(n)
        total = 0
        while dsu.components > 1 and edge_heapq.top():
            w, u, v = edge_heapq.pop()
            if not dsu.union(u, v):
                continue
            total += w
        
        return total if dsu.components == 1 else -1