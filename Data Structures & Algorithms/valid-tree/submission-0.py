class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
       #Base case when the graph is empty.
       #Any empty graph technically counts as a tree.
        if not n:
            return True 
        #initialise a hashmap where the key is the node and the value is any empty list thats gonna be storing its neighbours
        adj = {i:[] for i in range(n)}

        #Then go through every pair of nodes(a single edge).
        #Remember the edges are not directed
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        #keep track of the visited nodes
        visit = set()

        #define the dfs algo and make sure to pass both the current or prev
        def dfs(i, prev):
            #This is the first base case
            if i in visit:
                return False
            #if not in visit, then visit it
            visit.add(i)
            #Then we need to go through its neighbour

            for j in adj[i]:
                if j == prev:
                    continue
                #if its not the prev node we came from then we are gonna call dfs on j and we pass in i as prev coz thats where we are coming from
                #And if that returns false, then you need to return false immediately
                if not dfs(j, i):
                    return False

            #If we go through every single neighbour without detecting False, then return True
            return True

        #Lets do the initial calling. DFS is gonna check the existence of a loop while n==len(visit) checks if the graph is coonnected
        return dfs(0,-1) and n==len(visit)




        