class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, 0
        res = []
        n = len(nums)

        while r < n and nums[r] < 0:
            r += 1

        l = r - 1

        while l >= 0 and r < n:
            if abs(nums[l]) <= abs(nums[r]):
                res.append(nums[l] ** 2)
                l -= 1
            else:
                res.append(nums[r] ** 2)
                r += 1

        while l >= 0:
            res.append(nums[l] ** 2)
            l -= 1

        while r < n:
            res.append(nums[r] ** 2)
            r += 1

        return res
        


        


     

 

      



        




