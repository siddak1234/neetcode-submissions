class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i, a in enumerate(nums):
            diff = target - a
            if diff in hash:
                return [hash[diff], i]
            hash[a] = i

            