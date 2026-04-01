class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def dfs(course):
            if course in visit:
                return adj[course]
            next_courses = adj[course].copy()
            for next_course in next_courses:
                ret = dfs(next_course)
                for follow in ret:
                    adj[course].add(follow)
            visit.add(course)
            return adj[course]

        adj = [set() for _ in range(numCourses)]
        for prereq, course in prerequisites:
            adj[prereq].add(course)
        
        visit = set()
        for course in range(numCourses):
            dfs(course)
        
        return [vj in adj[uj] for uj, vj in queries]