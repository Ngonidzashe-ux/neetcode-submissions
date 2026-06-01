class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #My own approach
        # mainlist = []
        # for i in range(len(strs)):
        #     sublist = []
        #     j = i + 1
        #     for j in range(len(strs)):
        #         if sorted[strs[i]] == sorted[strs[j]]:
        #             sublist.append(strs[i])
        #             sublist.append(strs[j])
        # mainlist.append(sublist)
        # return mainlist


        #The optimal approach
        hashmap = defaultdict(list) #mapping the character count to List of anagrams
        for i in strs:
            count = [0] * 26 #a ....z. Map a to index 0.
            for c in i:
                count[ord(c) - ord("a")] += 1

            hashmap[tuple(count)].append(i)
        return hashmap.values()
        
        #lists cant be keys coz keys of a dictionary need to be immutable 
        #So we need to change the count from a list to a tuple