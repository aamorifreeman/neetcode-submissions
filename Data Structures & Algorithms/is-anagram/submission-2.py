class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        norm_s = [0] * 26
        norm_t = [0] * 26

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            index_s = ord(s[i]) - ord('a')
            index_t = ord(t[i]) - ord('a')
            
            norm_s[index_s] += 1
            norm_t[index_t] += 1
        
        return norm_s == norm_t




        