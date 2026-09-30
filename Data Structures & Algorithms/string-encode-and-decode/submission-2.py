class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for word in strs:
            word_length = len(word)
            new_word = str(len(word)) + '#' + word
            res += (new_word)
        return res
        
    def decode(self, s: str) -> List[str]:
        
        res = []
        l = 0
        while l < len(s):
            r = l

            while s[r] != '#':
                r += 1
           
            word_length = int(s[l:r])
            word = s[r + 1: word_length + r + 1]
            res.append(word)
            
            l = r + 1 + word_length
        
        return res


        

