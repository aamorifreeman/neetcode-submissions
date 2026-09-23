class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq_map = {}
        for word in strs:
            
            # counting freq
            freq_count = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                freq_count[index] += 1
            
            norm_word = tuple(freq_count)
            if norm_word in freq_map:
                freq_map[norm_word].append(word)
            else:
                freq_map[norm_word] = [word]
        return list(freq_map.values())






        




        