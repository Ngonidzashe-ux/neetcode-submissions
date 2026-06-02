"""

Understand:
Given a string, encode it into a list of strings.
Given a list of strings, decode it into the orginal string
Edge cases. String list could be empty or the the actual string could be empty.
Constraints. Any possible character out of the 256 ascii characters

Match. This is the first of this kind

Plan:
Encoding could be using the ord values of their characters. Maybe could even add a consistent number like 7.
Then after finishing each word, then add a #
to mark the end of a string

encodedList = []
for each word in strs:
    for each ch in word:
        encodedList.append(str(ord(char) + 7))
    encodedList.append("#")



"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        self.encodedList = []
        for word in strs:
            for ch in word:
                self.encodedList.append(chr(ord(ch) + 7))
            self.encodedList.append("#")
        print(self.encodedList)
        return "".join(self.encodedList)
            
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        output = []
        strings = s.split('#')
        print(strings)
        for word in strings[: len(strings) - 1]:
            temp = []
            for c in word:
                temp.append(chr(ord(c) - 7))
            output.append("".join(temp))
        return output
            




