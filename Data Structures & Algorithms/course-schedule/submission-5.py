"""
Understand:
- Return True or False on if you can finish all the courses you need to take
- Input: List, int: Output: Bool
- Constraints: 1 <= numCourses <= 1000
- Edge cases: Numcourses is 0, prereq is empty, course is its own prerequisite

Match:
Like Clone Graph, this problem uses an adjacency list. Like number of islands, we have to use dfs and lookout for cycles
Plan:

"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses:
            return True
        graph = collections.defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        path = set()
        visited = set()
        def dfs(node):
            # if not node:
            #     return True
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
       

        
        