class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = set()
        max_count = 0
        l = 0
        for r in range(len(s)):
            curr_char = s[r]
            while curr_char in char_set:
                char_set.remove(s[l])
                l += 1
            
            char_set.add(curr_char)
            curr_len = r - l + 1
            max_count = max(max_count, curr_len)
        return max_count


        
        