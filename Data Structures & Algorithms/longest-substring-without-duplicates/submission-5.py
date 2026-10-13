class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        l = 0
        max = 0
        for r in range(len(s)):
            if s[r] has been seen before:
                while s[r] in my set:
                    remove s[l] from set
                    l += 1
            
            add char to my set
            max = max(max, r - l + 1)
        return max
        """

        l = 0
        max_len = 0
        seen_window = set()
        for r in range(len(s)):
            while s[r] in seen_window:
                seen_window.remove(s[l])
                l += 1
            
            seen_window.add(s[r])
            max_len = max(max_len, r - l + 1)
        return max_len





        
        