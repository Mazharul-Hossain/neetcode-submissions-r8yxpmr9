import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_counter = collections.Counter(s)
        for c in t:
            if c not in char_counter:
                return False

            char_counter[c] -= 1
            if char_counter[c] == 0:
                del char_counter[c]
        
        return len(char_counter) == 0


