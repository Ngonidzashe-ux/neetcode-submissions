"""
Understand: 
- Encode a list of strings into a single string and then decode the string into a list of strings
- encode: Input = list of strings, output = string
- decode: input = string, output = list of strings
- Edge cases: strs = [], strs can have any string
- Constraints = Need to be able to decode the encoding uniquely

Match:
- This is the first problem of its sort that I am coming accross


Plan:
Encode:
- if strs is Emptry, return empty string
- Use a list instead of a string coz string modification creates a new string all the time.
- res = []
- for word in strs:
    length = str(len(word))
    res.append(length)
    res.append('#')
    for i in word:
        res.append(i)

return "".join(res)

Decode:
if len(s) == 0:
    return []
res = []
start, i = 0, 0
while i < len(s):
    if s[i] == '#':
        length = int(s[start:i])
        word = s[i+1: i+1+length]
        res.append(word)
        i = i+1+length
    else:
        i+=1
return res


"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = []
        for word in strs:
            length = str(len(word))
            res.append(length)
            res.append("#")
            for i in word:
                res.append(i)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res = []
        start, i = 0, 0
        while i < len(s):
            if s[i] == "#":
                length = int(s[start:i])
                word = s[i+1:i+1+length]
                res.append(word)
                i = start = i+1+length
            else:
                i+=1
        return res
