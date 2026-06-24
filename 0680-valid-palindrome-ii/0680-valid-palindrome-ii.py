class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        a = 0
        b = len(s)-1
        while s[a] == s[b] and a<b:
            a+=1
            b-=1
        if a>=b:
            return True
        
        m = s[a:b]
        n = s[a+1:b+1]
        if m == m[::-1]:
            return True
        if n == n[::-1]:
            return True
        return False