class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        while n:
            # if n & 1:
            #     answer += 1
            
            # n = n >> 1
            n = n & (n - 1)
            answer += 1
            # print(bin(n))
        
        return answer

    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(n+1):
            answer.append(self.hammingWeight(i))

        return answer