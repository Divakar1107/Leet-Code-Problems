class Solution:
    def search(self, nums: List[int], target: int) -> int:
        targets=0
        for num in nums:

            if num == target:
                return targets

            else:
                targets+=1

        return -1


            

        