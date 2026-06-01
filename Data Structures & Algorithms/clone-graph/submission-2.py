"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
"""
dfs(node)'s purpose is to create a copy of a node
So if given node is None, return None, 
If given Node has been created, return the created node
Otherwise create the node
Add it to the visited dictionary
For each of the original node's neigbors, create a coppy and append it to the neighbors of the copy
After that, then return the copyNode
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = collections.defaultdict(Node)

        def dfs(node):
            if not node:
                return None
            if node in visited:
                return visited[node]
            copyNode = Node(node.val)
            visited[node] = copyNode
            for nei in node.neighbors:
                copyNode.neighbors.append(dfs(nei))
            return copyNode
        return dfs(node)

