class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first=-1

        for i in range(len(nums)):
            if nums[i]==target:
                if first==-1:
                    first=i

        return first
        