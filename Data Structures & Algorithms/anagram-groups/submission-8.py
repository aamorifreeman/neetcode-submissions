from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        for word in strs:
            for each char in word:
                calculate index postion based on char
                increment at index in norm array

            if check if norm_array in dict:
                append orignal str to the keys value list
            else:
                add the key to our dict and intialize value to an array with orginal strs    
        
        """
        # anagr_map = {}
        # for word in strs:
            
        #     norm_word = 26 * [0]
            
        #     for char in word:
        #         index = ord(char) - ord('a')
        #         norm_word[index] += 1
            
        #     norm_word = tuple(norm_word)
            
        #     if norm_word in anagr_map:
        #         anagr_map[norm_word].append(word)
        #     else:
        #         anagr_map[norm_word] = [word]
        
        # return list(anagr_map.values())

        anagr_map = defaultdict(list)
        for word in strs:
            norm_word = 26 * [0]
            
            for char in word:
                index = ord(char) - ord('a')
                norm_word[index] += 1
            
            norm_word = tuple(norm_word)
            anagr_map[norm_word].append(word)
        
        return list(anagr_map.values())

        







            







        




        