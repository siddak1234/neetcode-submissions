class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, cur = 0, 0
        for n in nums:
            if n == 1:
                cur+=1
                if cur>res:
                    res+=1
            else:
                cur=0
        return res