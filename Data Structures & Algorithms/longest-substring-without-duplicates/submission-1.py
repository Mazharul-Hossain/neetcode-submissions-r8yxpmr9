class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        left = -1
        index_map = {}
        for i, c in enumerate(s):
            if c in index_map and left < index_map[c]:
                left = index_map[c]

            index_map[c] = i
            answer = max(answer, i - left)
            # print(i, c, answer)
        return answer