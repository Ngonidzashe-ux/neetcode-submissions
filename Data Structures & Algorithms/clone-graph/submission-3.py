"""
Understand: 
Return a deep copy of a graph.
Input: Node: node, Output Node
Constraints: 1- indexed
Edge cases: Null Node, cycles, duplicate node values, disconnected graph
Match: Like Other graph problems, this involves dfs
Plan:
If node is None:
    return None
visited to track the visited and the copies of that
in dfs, base case is returning something
return None if you hit a null
If you hit visited, return the copy
Otherwise create a new node and put the value in, update visited
return dfs(node)

"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}
        def dfs(node):
            if not node:
                return None
            if node in visited:
                return visited[node]
            newNode = Node(node.val)
            visited[node] = newNode
            for nei in node.neighbors:
                newNode.neighbors.append(dfs(nei))
            return newNode
        return dfs(node)
        

        
