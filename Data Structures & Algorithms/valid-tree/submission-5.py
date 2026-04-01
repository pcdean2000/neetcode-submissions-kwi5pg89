class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        if n == 1:
            return True

        seen = set()
        malicious = []
        seen.add(edges[0][0])
        
        for n1, n2 in edges:
            if n1 in seen and n2 in seen:
                return False
            if not (n1 in seen or n2 in seen):
                malicious.append([n1, n2])
                continue
            seen.add(n1)
            seen.add(n2)

        malicious.sort()

        for n1, n2 in malicious:
            if n1 in seen and n2 in seen:
                return False
            seen.add(n1)
            seen.add(n2)

        return True