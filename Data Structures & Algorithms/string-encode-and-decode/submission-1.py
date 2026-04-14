class Solution:

    def encode(self, strs: List[str]) -> str:
        answer = ""
        for word in strs:
            answer += f"{len(word)}#{word}#"
            # print("encode:", answer)

        # print("encode:", answer)
        return answer

    def decode(self, s: str) -> List[str]:
        # print("decode:", s)

        mode = "number"
        length = 0
        word = ""

        answer = []
        i, N = 0, len(s)

        while i < N:
            # print("decode:", s[i], mode, word, length)

            if mode == "number":
                if s[i] == "#":
                    
                    mode = "str"
                    word = ""
                
                else:
                    length = 10 * length + int(s[i])
            
            else:
                if length > 0:
                    word += s[i]
                    length -= 1
                
                else:
                    answer.append(word)

                    mode = "number"
                    length = 0
            
            i += 1
        
        return answer