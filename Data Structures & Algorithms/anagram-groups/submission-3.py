class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = {}
        
        for word in strs:
            norm_word = {}
            for char in word:
                if char in norm_word:
                    norm_word[char] += 1
                else:
                     norm_word[char] = 1
            norm_word = tuple(sorted(norm_word.items()))
            
            if norm_word in seen:
                seen[norm_word].append(word)
            else:
                seen[norm_word] = [word]
        
        res = []
        for key in seen:
            res.append(seen[key])

        return res




        




        