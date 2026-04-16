class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        g_ord = lambda a: ord(a) - ord("a")
        if len(s1) > len(s2):
            return False

        L = len(s1)
        need = [0] * 26
        for i in range(L):   # O(L)        
            c = g_ord(s1[i])
            need[c] += 1
        # print(need)
        
        # print("# initial window") 
        window = [0] * 26
        for i in range(L):   # O(L)
            c = g_ord(s2[i])            
            window[c] += 1
        # print(window)

        # print("# matches in initial window")
        match = 0
        for c in range(26):
            if window[c] == need[c]:
                match += 1
        # print("match:", match)

        left, M = 0, len(s2)
        for i in range(L, M):  # O(M - L)
            if match == 26:
                # print(match, window)
                # Final time complexity: O(M + L)
                return True

            # add right
            c = g_ord(s2[i])
            
            if window[c] == need[c]:
                match -= 1   # was matching, now will break

            window[c] += 1

            if window[c] == need[c]:
                match += 1   # now becomes matching

            # print("->", i, c, match, window)

            # remove left
            c2 = g_ord(s2[left])
            
            if need[c2] == window[c2]:
                # print(c2, -1, need[c2], window[c2])
                match -= 1   # was matching, now will break

            window[c2] -= 1

            if need[c2] == window[c2]:
                # print(c2, +1, need[c2], window[c2])
                match += 1   # now becomes matching

            left += 1
            # print(match, window)
            
        # Space complexity: O(M + L)
        return match == 26