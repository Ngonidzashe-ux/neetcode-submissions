class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for neigh in graph[node]:
                if neigh == prev:
                    continue
                if not dfs(neigh, node):
                    return False
            return True
                
        return dfs(0, -1) and n == len(visited)

