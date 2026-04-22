        answer = 0
        while n:
            # if n & 1:
            #     answer += 1
            
            # n = n >> 1
            # print(bin(n))
        
            n = n & (n - 1)
            answer += 1
        return answer
        
class Solution:
    def hammingWeight(self, n: int) -> int: