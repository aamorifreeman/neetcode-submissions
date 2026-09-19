class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = {}
        for word in strs:
            norm_word = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                norm_word[index] += 1
            
            norm_word = tuple(norm_word)
            
            if norm_word in seen:
                seen[norm_word].append(word)
            else:
                seen[norm_word] = [word]
        
        res = []
        for key in seen:
            res.append(seen[key])

        return res




        




        