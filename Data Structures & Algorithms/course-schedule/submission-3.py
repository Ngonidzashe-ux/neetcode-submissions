"""
Understand:
- Need to come up with a graph in adjacency list format where the course has its prereqs as its neighbours
- Then go through each course, if a course has not been visited then we explore it
- In this exploration, return True if there are no cycles, return False if cycles and this shows that we can't complete this course


dfs(node):
If the node is in visited, which means has been explored and we know that its completable, then return True
If the node is in the present path of this traversal, then return False
Otherwise, 
add the node to the path, then traverse through its neigbours
If the neighbours are good
Then we come back, remove the node from the path, then add it to the visited set
Then return True

"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        visited = set()
        path = set()


        def dfs(node):
            if node in visited:
                return True
            if node in path:
                return False

            path.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            path.remove(node)
            visited.add(node)
            return True

        for node in range(numCourses):
            if node not in visited:
                if not dfs(node):
                    return False
        return True

        
        