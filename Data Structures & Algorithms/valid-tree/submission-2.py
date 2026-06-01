"""
Understand:
- Valid Tree: Fully connected, no cycles


Plan:
- Construct a graph using the adjacency list
- Initialise a path set to track the visited nodes to note cycles
- Then run a dfs on any one node
- Dfs should take in curr node and parent
- If the curr node is in path, then return false
- Otherwise add it to the path
- Then for each nei, if its not the parent, then run a dfs on it
- Then return true if no cycles
- In the main function, check if the len of path is equal to number of nodes

"""


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        

        path = set()

        def dfs(node, par):
            if node in path:
                return False
            path.add(node)
            for nei in graph[node]:
                if nei == par:
                    continue
                else:
                    if not dfs(nei, node):
                        return False
            return True

        if dfs(0, -1) and len(path) == n:
            return True
        return False
        