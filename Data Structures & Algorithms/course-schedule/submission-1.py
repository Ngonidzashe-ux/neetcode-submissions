
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build the adjacency list graph
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        visited = set()  # Tracks nodes in the current DFS path, no need to pass it as a parameter cause its global and our function dfs is nesteed
        # Step 2: DFS function to detect cycles
        def dfs(node):
            if node in visited:  # Cycle detected
                return False
            if not graph[node]:  # No prerequisites, course can be completed
                return True

            visited.add(node)  # Mark as visiting
            for prereq in graph[node]:
                if not dfs(prereq):  # Recursively check prerequisites
                    return False

            visited.remove(node)  # Backtrack after processing
            graph[node] = []  # Mark course as safe (pruned for efficiency)
            return True

        # Step 3: Check all courses (handles disconnected graphs)
        for course in range(numCourses):
            if not dfs(course):
                return False  # Cycle found, cannot finish all courses

        return True  # No cycles, all courses can be completed
