"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
Understand:
Creat a deep copy of a linked list that has random pointers too. 
Input: Node, Output: head of new List
Edge Cases: Empty list in the beginning or one

Match: Like Graph Clone, we need to create a hashMap mapping old nodes to new nodes so we dont have recreate visited ones
Like Graph Clone, it seems using dfs and treating this as a graph might work
Plan:

"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        visited = {}
        def dfs(node):
            if not node:
                return
            if node in visited:
                return visited[node]
            newNode = Node(node.val)
            visited[node] = newNode
            newNode.random = dfs(node.random)
            newNode.next = dfs(node.next)

            return newNode
        return dfs(head)
