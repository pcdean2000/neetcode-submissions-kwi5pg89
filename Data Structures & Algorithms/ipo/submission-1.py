class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        def update():
            while pq_capitals and w >= pq_capitals[0][0]:
                _, i = heapq.heappop(pq_capitals)
                heapq.heappush(pq_profits, -profits[i])
        
        pq_profits = []
        pq_capitals = [(cost, i) for i, cost in enumerate(capital)]
        heapq.heapify(pq_capitals)
        
        update()

        for _ in range(k):
            if not pq_profits:
                return w
            w -= heapq.heappop(pq_profits)
            update()
        
        return w