class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #Initialise our two arrays
        par = [i for i in range(n)]
        rank = [1]*n

        #This is to find the root parent of n1
        #The root parent is always the one that is the parent of itself
        def find(n1):
            res = n1
            #if the node is not the parent of itself, then its not a root node and you would have to traverse back to the root node
            while res != par[res]:
                #Setting the parent of the result equal to its grandparent
                # par[res] = par[par[res]] - This is path compression used to optimize union find problems
                par[res] = par[par[res]] 
                #Make the parent the current result so we can check its parent and traverse up the path
                res = par[res]
            return res

        def union(n1,n2):
            #Find the roots of n1 and n2
            p1, p2 = find(n1), find(n2)
            #if they are the same, then they are merged already and return 0 to show that you did not end up merging
            if p1 == p2:
                return 0

            #If they are not merged, you want to figure out which one has the higher rank and make that the parent of the other one
            if rank[p2]> rank[p1]:
                #make the parent of p1 = p2 if p2 has a higher rank
                par[p1] = p2
                #since you have added a child to p2, you need to increment its rank by adding the rank of p1 which is the recently connected child
                rank[p2]+= rank[p1]
            else: 
                par[p2] = p1
                rank[p1]+= rank[p2]
            #After updating of the arrays, return 1 to show that the union is successful
            return 1
        #Initialising the initial number of the connected components
        res = n
        for n1, n2 in edges:
            #Then iterate through each edge and then subtract the result of the union n1, n2
            res -= union(n1,n2)
        return res
