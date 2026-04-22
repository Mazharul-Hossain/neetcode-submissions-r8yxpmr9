class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        indegree = {c: 0 for word in words for c in word}

        for w1, w2 in zip(words, words[1:]):
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indegree[c2] += 1
                    break
        
        # print(adj)

        queue = deque([c for c in indegree if indegree[c] == 0])
        answer = []
        while queue:
            c = queue.popleft()
            answer.append(c)

            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
            # When a longer word appears before its own prefix (e.g., "abc" before "ab"), 
            # this is an invalid ordering that cannot exist in any alphabet. 
            # Failing to detect this case and return an empty string leads to incorrect 
            # results or undefined behavior.
        return "".join(answer) if len(answer) == len(indegree) else ""