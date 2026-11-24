class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}#saves numbers and their indexes
        for i,num in enumerate(nums):
            compliment = target - num
            if compliment in seen:
                return[seen[compliment],i]
            seen[num] = i