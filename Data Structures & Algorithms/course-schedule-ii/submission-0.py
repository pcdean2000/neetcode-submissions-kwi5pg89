class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            state[course] = 1
            for req in adj[course]:
                if not dfs(req):
                    return False
            topo.append(course)
            state[course] = 2
            return True
        
        adj = [[] for _ in range(numCourses)]
        for course, req in prerequisites:
            adj[course].append(req)
        
        topo = []
        state = [0 for _ in range(numCourses)]
        for course in range(numCourses):
            if not dfs(course):
                return []
        return topo