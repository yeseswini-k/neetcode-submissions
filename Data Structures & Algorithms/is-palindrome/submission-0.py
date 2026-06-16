class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1= s.lower()
        s2=""
        for ch in s1:
            if ch.isalnum():
                s2= ch+ s2

        if s2[::]==s2[::-1]:
            return True
        else:
            return False
            