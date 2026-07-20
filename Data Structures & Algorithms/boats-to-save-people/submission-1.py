class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        people.sort()
        
        l, r = 0,len(people)-1

        while l<=r:
            diff = limit-people[r]
            r-=1
            res+=1
            if people[l]<=diff:
                l+=1
        return res
                    
