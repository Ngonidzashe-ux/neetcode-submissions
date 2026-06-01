class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #This is an adj list based on the ordering of the characters
        #We want every character to be mapped to a word.
        adj = {char: set() for word in words for char in word}

#We are gonna go through each pair of words
        for i in range(len(words) - 1):
            #Get the pair
            w1, w2 = words[i], words[i + 1]
            #Get the minimum length between these 2 words
            minLen = min(len(w1), len(w2))
            #The edge case where word w1 is longer than w2 yet w2 is a prefix of w1, then we have an invalid ordering
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            #If thats not the case, we want to go through every single character in these words
            for j in range(minLen):
                #Our goal is to find the first different character
                if w1[j] != w2[j]:
                    #Then we want to say the character in w2 comes after the character in w1
                    #We do that by adding the w2 character to the list of w1.
                    adj[w1[j]].add(w2[j])
                    #Then break because we are interested in only the first different character between the words
                    break

        visited = {}  # {char: bool} False visited, True current path
        res = []

#We want to pass in the current char or node
        def dfs(char):
            #if the char has been visited return its value
            if char in visited:
                #If visited[char] is False, this means the char has been visited so we return False 
                #If visited[char] is True, this means we saw a char or node that was already in the current path and we saw it twice and this means we detected a loop
                return visited[char]
#If the above is not met, then we are gonna set the node to True to say that we have visited the node and its also in the current path
            visited[char] = True
#We are gonna go thorough each char(neighbour) that comes after the current char and run dfs on it
            for neighChar in adj[char]:
                #If this is true, then return true immediately because there is a loop
                if dfs(neighChar):
                    return True
            #If there is no loop while traversing the neighbours, then remove the node from the current path by setting visited to false
            visited[char] = False
            #then append the char
            res.append(char)
        #Now lets call the dfs, for each char or node in the adj list. We don't need to start at the beginning of the graph. Should work from any char
        for char in adj:
            #if this returns true, return an empty string because this means there is a loop
            if dfs(char):
                return ""
#if thats not the case, reverse the result and then join to form a string
        res.reverse()
        return "".join(res)
  