class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        
        for n in nums:
            if (n-1) not in nums:
                length = 0
                while(n+length) in numset:
                    length+=1
                res = max(length, res)
        return res