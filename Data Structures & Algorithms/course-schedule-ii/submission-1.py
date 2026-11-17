class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        visited = set()
        cycle = set()
        output = []

        def dfs(crs):
            if crs in cycle:
                return False 
            if crs in visited:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            
            visited.add(crs)
            cycle.remove(crs)
            output.append(crs)
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        
        return output