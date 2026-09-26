class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
        seen set = {}
        max_sub = 0
        l = 0
        
        for r in range(len(s)):
            char = s[r]
            while char in seen:
                seen.remove[s[l]]
                l += 1
            
            seen.add(seen)
            curr_max = len(seen)
            max_sub = max(max_sub, curr)
        return max_sub


        """

        seen = set()
        max_sub = 0
        l = 0
        
        for r in range(len(s)):
            char = s[r]
            while char in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(char)
            curr_max = len(seen)
            max_sub = max(max_sub, curr_max)
        return max_sub


        
        