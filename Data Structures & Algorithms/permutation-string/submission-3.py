class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Personal Attempt
        #Sorting algorithm is n log n and then times the n of the while loop
        # l, r = 0, (len(s1)-1)
        # while r < len(s2):
        #     x1 = sorted(s1)
        #     x2 = sorted(s2[l:r+1])

        #     if x1 == x2:
        #         return True
        #     else:
        #         l+=1
        #         r+=1
        # return False
        if len(s1) > len(s2):
            return False
        #Better to always use hashmaps to compare character frequencies
        list1, list2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            list1[ord(s1[i])- ord('a')] += 1
            list2[ord(s2[i])- ord('a')] += 1

        matches = 0
        for i in range(len(list1)):
            if list1[i] == list2[i]:
                matches+=1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            #Remove far left and check matches
            index_of_far_left = ord(s2[l]) - ord('a')
            list2[index_of_far_left] -=1
            if list1[index_of_far_left] == list2[index_of_far_left]:
                matches+=1
            elif list1[index_of_far_left]-1 == list2[index_of_far_left]:
                matches -=1

            #Add immediate right and check matches
            index_of_imm_right= ord(s2[r]) - ord('a')
            list2[index_of_imm_right] +=1
            if list1[index_of_imm_right] == list2[index_of_imm_right]:
                matches+=1
            elif list1[index_of_imm_right]+1 == list2[index_of_imm_right]:
                matches -=1
            l+=1

        return matches == 26


        


   

        