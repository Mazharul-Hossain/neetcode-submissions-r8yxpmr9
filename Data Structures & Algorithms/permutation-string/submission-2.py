class Solution:
    def checkMap(self, counter1, counter2) -> bool:
        for c, f in counter1.items():
            if c not in counter2 or counter2[c] != f:
                return False
            # print(c, f, counter2[c])
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counter = collections.Counter(s1)
        # print(counter)
        
        L = len(s1)
        search_counter = collections.Counter()
        for i in range(L - 1):
            if s2[i] in counter:
                search_counter[s2[i]] += 1
        
        left, M = 0, len(s2)
        for i in range(L - 1, M):
            if s2[i] in counter:
                search_counter[s2[i]] += 1
            
            # print(search_counter)
            if len(counter) == len(search_counter) and self.checkMap(counter, search_counter):
                return True
            
            if s2[left] in search_counter:
                search_counter[s2[left]] -= 1
                if search_counter[s2[left]] == 0:
                    del search_counter[s2[left]]
            left += 1
            
        return False