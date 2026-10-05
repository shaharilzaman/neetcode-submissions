class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #intilaizes each key val pait to be course num to empty list 
        path = {i:[] for i in range(numCourses)} 
        for crs, preq in prerequisites:
            path[crs].append(preq)
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if path[crs] == "":
                return True
            visited.add(crs)
            for preq in path[crs]:
                if not dfs(preq):
                    return False 
            visited.remove(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True