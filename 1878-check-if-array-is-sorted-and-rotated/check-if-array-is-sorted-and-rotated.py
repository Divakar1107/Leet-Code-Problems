class Solution:
    def check(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            
            rotated=nums[-i:]+nums[:-i]

            if rotated==sorted(rotated):
                return True

        return False



        