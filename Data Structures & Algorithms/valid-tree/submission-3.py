"""
Understand:
Return true if the graph does not have cycles and is fully connected
Input: int n, edges List[List[int]], Output: True / False
Constraints 1 < n < 100
Edge cases: 0 nodes, empty edge list
Match: Like Course Schedule we have to create an adjacency list of a graph and detect cycles
Match: Like Course Schedule we start from one point and by the time we finish that, if we have not visited all the nodes, then not connected
Plan:
if not n or not edges:
    return True
graph = collections.defaultdict(list)
for n1, n2 in edges:
    graph[n1].append(n2)
    graph[n2].append(n1)

visited, path = set(), set()
def dfs(node):
    if node in path:
        return False
    if node in visited:
        return True
    path.add(node)
    for nei in graph[node]:
        if not dfs(nei):
            return False
    path.remove(node)
    visited.add(node)
    return True
return dfs(0) and len(visited) == n
"""


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False
        graph = collections.defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            print(visited)

            return True
        return dfs(0, -1) and len(visited) == n
        
        