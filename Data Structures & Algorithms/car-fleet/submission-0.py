class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        
        answer = 1
        #sort by time: s = vt
        prev_time = (target - pair[0][0]) / pair[0][1]
        for (p, s) in pair:
            cur_time = (target - p) / s
            if prev_time < cur_time:
                answer += 1
                prev_time = cur_time

        return answer
        