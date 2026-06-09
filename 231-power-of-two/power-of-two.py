class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        x=0
        while n>=pow(2,x):
            if n==pow(2,x):
                return True

            x+=1

        return False

        


        