class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Adjacency list mapping the course to its prerequisites
        #This is the initialisation process
        preMap = {i: [] for i in range(numCourses)}

        #We are gonna go through the course prerequisite pair in the prerequisites list and add them to their corresponding lists in the map
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        #Create a visiting set that is going to store the courses or nodes visited in the current dfs
        visiting = set()

        #Defining our dfs function that we are going to use for each course

        def dfs(crs):

            #Base case 1, if the crs has been visited already, return false, coz that is a loop
            if crs in visiting:
                return False
            #If the course does not have any prerequisite then we need to return True immediately
            if preMap[crs] == []:
                return True

            #If these conditions are not met, then we visit it and add it to the visiting set
            visiting.add(crs)
            #Iterate through the preq to check if they have their own prereq
            for pre in preMap[crs]:
                #If a course returns False which means it cant be completed from running dfs on it, then immediately return False
                if not dfs(pre):
                    return False
            #If we went through all the prereq courses and never ended up adding the current course in the visit set, this means that there is no cycles and loops that the course is in and therefore we remove it from the visiting set so the visitng
            #set is ready for the remaining courses
            visiting.remove(crs)
            #Then reset the course to have an empty list to show that this course can be done
            preMap[crs] = []
            #return ture
            return True

#Go through each node or course just in case we have a disconnected graph
        for c in range(numCourses):
            #If the dfs returns False which means the course can't be completed, then immediately return False which means not all the courses can be done

            if not dfs(c):
                return False

        #If not, then return True
        return True