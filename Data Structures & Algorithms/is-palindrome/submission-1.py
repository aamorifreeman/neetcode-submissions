class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        res = ""
        for char in s:
            if char.isalnum():
                res += char
        s_norm = res.lower()

        l = 0
        r = len(s_norm) - 1

        while(l < r):
            if s_norm[l]!=s_norm[r]:
                return False
            else:
                l += 1
                r -=1
        return True

            

        