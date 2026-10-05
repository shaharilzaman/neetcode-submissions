class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #intilaizes each key val pait to be course num to empty list 
        path = {i:[] for i in range(numCourses)} 
        for course, prereq in prerequisites:
            path[course].append(prereq)
        visit = set()
        def dfs(course):
            if course in visit:
                return False 
            if path[course] == []:
                return True
            
            visit.add(course)
            for prereq in path[course]:
                if not dfs(prereq):
                    return False
            visit.remove(course)
            path[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True 