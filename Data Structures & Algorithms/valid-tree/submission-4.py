class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edges.sort()
        seen = set()
        # malicious = set()
        seen.add(0)
        
        for n1, n2 in edges:
            if n1 in seen and n2 in seen or not (n1 in seen or n2 in seen):
                return False
            # if not (n1 in seen or n2 in seen):
            #     malicious.add((n1, n2))
            #     continue
            seen.add(n1)
            seen.add(n2)

        # for n1, n2 in malicious:
        #     if (n1 in seen and n2 in seen) or not (n1 in seen or n2 in seen):
        #         return False
        #     seen.add(n1)
        #     seen.add(n2)

        return True