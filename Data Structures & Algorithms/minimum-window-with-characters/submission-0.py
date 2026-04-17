class Solution:
    def minWindow(self, s: str, t: str) -> str:
        g_ord = lambda a: ord(a) - ord("a")
        if len(t) > len(s):
            return ""

        L = len(t)
        need = collections.Counter(t)   # O(L)
        # print(need)
        
        min_len, answer = float("inf"), ""
        match = 0
        left, M = 0, len(s)
        window = {}
        for i in range(M):  # O(M)
            # expand right →
            #     until valid

            # add right            
            c = s[i]
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                match += 1   # now becomes matching
            # print("->", i, c, match, window)

            while match == len(need) and left <= i:
                # shrink left →
                #     until invalid

                if min_len > i - left + 1:
                    min_len = i - left + 1
                    answer = s[left: i + 1]
                    # print(left, i, answer)

                c2 = s[left]                
                if c2 in need and need[c2] == window[c2]:
                    # print(c2, -1, need[c2], window[c2])
                    match -= 1   # was matching, now will break

                window[c2] -= 1
                left += 1
                # print(match, window)
            
        # Space complexity: O(M + L)
        return answer