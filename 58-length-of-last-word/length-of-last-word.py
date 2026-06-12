class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s.split()
        for i in s:
            if a!="":
                return len(a[-1])

                

        