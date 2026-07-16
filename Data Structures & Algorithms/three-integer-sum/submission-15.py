class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        tri = []
        nums.sort()

        def ksum(k, start, target):
            if k!=2:
                for i in range(start, len(nums)-k+1):
                    if i>0 and nums[i] == nums[i-1]:
                        continue
                    tri.append(nums[i])
                    ksum(k-1, i+1, target-nums[i])
                    tri.pop()
                return
            l,r = start, len(nums)-1
            while l<r:
                if nums[l]+nums[r]>target:
                    r-=1
                elif nums[l]+nums[r]<target:
                    l+=1
                else:
                    res.append(tri+ [nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
            return 
        ksum(3,0,0)
        return res