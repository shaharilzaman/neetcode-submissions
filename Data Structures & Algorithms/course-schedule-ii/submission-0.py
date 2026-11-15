class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)} # map each course to their prereq 
        for crs, pre in prerequisites: #acutally maps every crs to their prereq
            prereq[crs].append(pre)
            
        output = []
        visited = set() #see if the crs has been visted at all
        cycle = set() #chekcs in our given path from crs all to its prepreq see if there is cycle

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True  #we already checked its poath adn it is okay
                
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False #if at any point in the path it deteccts a cycle it is entirely false
                
            visited.add(crs)
            cycle.remove(crs) #done with this current path so remove
            output.append(crs) #if the path is all good we know to add it to the output 
            return True 
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return output 
        