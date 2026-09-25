class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        res = ""
        for char in s:
            if char.isalnum():
                res += char.lower()
        
        l = 0
        r = len(res) - 1
        
        while(l < r):
            if res[l] == res[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

        