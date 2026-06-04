class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleared=""

        for i in s:
            if i.isalnum():
                cleared+=i.lower()

        return cleared==cleared[::-1]
        