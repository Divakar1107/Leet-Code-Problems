class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        a=[]
        count=0

        for i in range(len(nums)):
            if nums[i]!=val:
                a.append(nums[i])
   

        for i in range(len(a)):
            count=count+1

        return count
        '''

        k=0

        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1

        return k
      
    