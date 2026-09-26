class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        pairs = {}
        for word in strs:
            norm_word = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                norm_word[index] += 1

            word_key = tuple(norm_word)
            if word_key not in pairs:
                pairs[word_key] = [word]
            else:
               pairs[word_key].append(word)
        
        return list(pairs.values())
            







        




        