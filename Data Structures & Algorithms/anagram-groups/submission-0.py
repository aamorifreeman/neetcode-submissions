class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = {}
        
        for word in strs:
            norm_word = "".join(sorted(word))
            if norm_word in seen:
                seen[norm_word].append(word)
            else:
                seen[norm_word] = [word]
        
        res = []
        for word in seen:
            res.append(seen[word])

        return res




        




        