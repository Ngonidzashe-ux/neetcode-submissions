"""
Understand:
1. Number of connected components in the graph


Plan:
1. Express the graph in an adjacency list format
2. Have a dictionary where the keys are the nodes, the values are lists containing the node's neighbours
3. Then for each node, we do a dfs to see the reachable nodes
4. Mantain a connected variable
5. Visit set too
"""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        res = 0

        graph = collections.defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        

        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in graph[node]:
                dfs(nei) 

        for node in range(n):
            if node not in visit:
                dfs(node)
                res+=1

        return res

