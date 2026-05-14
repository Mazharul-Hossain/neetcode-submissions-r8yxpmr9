class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        answer = 0
        left, right = 0, len(people) - 1
        
        while left <= right:
            remain = limit - people[right]
            right -= 1

            answer += 1
            if left <= right and people[left] <= remain:
                left += 1
        
        return answer