"""
Encode: 
Input: List and Output = String
Can use a # to seperate the strings
Hello#World#.
for each word, add it to the string, add # and go on like that
#Hello#World

##ello

To address that, maybe add the lenght of the word, and a #
16#hello45# when you see #

Decode:
Input: String
Ouput:List
go through the string, when you find a # then take the previous string before a #.
There is repeated work here, for each workd, we go over it twice. Find the next # and then go back. We need to highlight that we have a new word first and the

"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        output = []
        for s in strs:
            output.append(str(len(s)) + '#' + s)
        return "".join(output)

        


    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        output = []
        i, j = 0, 0
        while (i < len(s)):
            if s[i] == '#':
                length = int(s[j:i])
                output.append(s[i+1:i+1+length])
                j=i+1+length
                i = j
            else:
                i+=1
        return output

