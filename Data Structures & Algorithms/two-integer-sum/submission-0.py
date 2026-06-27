class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i,n in enumerate(nums):
            solution = target - n
            if solution in hash:
                return[hash[solution], i]
            hash[n] = i
        return

            