class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = collections.Counter()

        max_target = 0
        left = 0
        answer = 0
        for i, c in enumerate(s):
            char_map[c] += 1
            max_target = max(max_target, char_map[c])

            while (i - left + 1) - max_target > k:
                char_map[s[left]] -= 1
                left += 1
            
            answer = max(answer, i - left + 1)
        
        return answer