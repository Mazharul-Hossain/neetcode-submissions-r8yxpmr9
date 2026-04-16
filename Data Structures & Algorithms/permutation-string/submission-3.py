class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        L = len(s1)
        need = collections.Counter(s1) # O(L)
        window = collections.Counter()
        # print(need)
        
        # initial window
        match= 0 
        for i in range(L):  # O(L)
            c = s2[i]

            if window[c] == need[c]:
                match -= 1   # was matching, now will break
            
            window[c] += 1

            if window[c] == need[c]:
                match += 1   # now becomes matching

            # print(i, c, window)

        left, M = 0, len(s2)
        for i in range(L, M):  # O(M - L)
            if match == len(need):
                # print(match, window)
                # Final time complexity: O(M + L)
                return True

            # add right
            c = s2[i]
            
            if window[c] == need[c]:
                match -= 1   # was matching, now will break

            window[c] += 1

            if window[c] == need[c]:
                match += 1   # now becomes matching

            # print("->", i, c, match, window)

            # remove left
            c2 = s2[left]
            
            if need[c2] == window[c2]:
                # print(c2, -1, need[c2], window[c2])
                match -= 1

            window[c2] -= 1

            if need[c2] == window[c2]:
                # print(c2, +1, need[c2], window[c2])
                match += 1

            left += 1
            # print(match, window)
            
        # Space complexity: O(M + L)
        return match == len(need) 