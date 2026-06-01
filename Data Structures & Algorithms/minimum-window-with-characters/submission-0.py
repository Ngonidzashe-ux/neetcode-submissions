class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #if t is empty, return empty
        if t == "":
            return ""
        
        #two hashmaps, countT is gonna keep track of the HAVE
        #window is gonna keep track of how many of the characters in t are in the current window
        countT, window = {}, {}
        #count the characters that are in T and update the hashmap
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        #Initialise have to 0. have basically keeps track of how many character conditions have been met.
        #Need keeps track of how many character conditions need to be satisfied
        have, need = 0, len(countT)
        #res = [left pointer, right pointer]
        #reslen to be initialised to infinity
        res, resLen = [-1, -1], float("infinity")
        #Begin at l=0
        l = 0
        #Right pointer which is gonna start from 0 and run through the whole string s
        for r in range(len(s)):
            #the current character c is going to be the current one pointed to by the right pointer
            c = s[r]
            #Then update the count of the character c in window hashmap
            window[c] = 1 + window.get(c, 0)
            #if the character c is in countT and the value of the character in both hashmaps, then the condition of that character has been met
            if c in countT and window[c] == countT[c]:
                #incement have
                have += 1
#when have and need are equal, then check if the length of the window is less than resLen
#if it is, then you need to update the res with the current left and right pointers and also the resLen 

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                #Then we are gonna move the window by shifting the left pointer by one
                #This means that we are gonna decrement the count of the character that is pointed at by the left pointer 
                window[s[l]] -= 1
                #And if the character was in countT and the count of the window is now less than that of countT, this means the condition of that character is no longer met and we should decrement have
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                #Then increment the left pointer
                l += 1
        #after the loop, then update l and r using res
        l, r = res
        #return the current window string and resLen is not float. if the resultlength is still infinitiy then return empty string
        return s[l : r + 1] if resLen != float("infinity") else ""
