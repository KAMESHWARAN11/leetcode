class Solution(object):
    def longestPalindrome(self, s):
        longest = ""
        for i in range(len(s)):
            left = i
            right = i
            while left >=0 and right < len(s) and s[left]==s[right]:
                    current = s[left:right+1]
                    if len(current) > len(longest):
                        longest = current 
                    left -=1
                    right +=1
            left = i
            right = i+1

            while left >=0 and right < len(s) and s[left]==s[right]:
                    current = s[left:right+1]
                    if len(current) > len(longest):
                        longest = current
                    left -=1
                    right +=1
        return longest                
        