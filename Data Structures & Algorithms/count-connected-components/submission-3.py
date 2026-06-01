class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adlist = [ [] for _ in range(n)]
        for n1, n2 in edges:
            adlist[n1].append(n2)
            adlist[n2].append(n1)
        res = 0
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbour in adlist[node]:
                dfs(neighbour)
        for node in range(n):
            if node not in visited:
                dfs(node)
                res+=1
        return res
