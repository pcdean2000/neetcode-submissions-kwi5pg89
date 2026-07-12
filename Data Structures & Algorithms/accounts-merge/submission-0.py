class DSU:
    def __init__(self, nodes) -> None:
        self.parent = {}
        self.rank = {}

        for node in nodes:
            self.parent[node] = node
            self.rank[node] = 1
    
    def find(self, node):
        parent = self.parent[node]
        
        while parent != self.parent[parent]:
            self.parent[parent] = self.parent[self.parent[parent]]
            parent = self.parent[parent]
        
        return parent
    
    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        
        if parent1 == parent2:
            return False
        
        if self.rank[parent2] > self.rank[parent1]:
            parent1, parent2 = parent2, parent1
        
        self.parent[parent2] = parent1
        self.rank[parent1] += 1
        
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_map = {}
        email_edge = []

        for account in accounts:
            name, emails = account[0], account[1:]
            prev = None
            for email in emails:
                email_map[email] = name
                if prev:
                    email_edge.append((prev, email))
                prev = email
        
        dsu = DSU(email_map.keys())
        for email1, email2 in email_edge:
            dsu.union(email1, email2)

        parent_map = defaultdict(list)
        for email in sorted(email_map.keys()):
            parent_map[dsu.find(email)].append(email)
        
        res = []
        for parent, emails in parent_map.items():
            res.append([email_map[parent]] + emails)
        
        return res





















