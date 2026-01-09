class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        posfix = [1] * n

        pre_accumulator = 1
        pos_accumulator = 1

        for i in range(n):
            prefix[i] = pre_accumulator
            pre_accumulator *= nums[i]

            j = (n - 1) - i
            posfix[j] = pos_accumulator
            pos_accumulator *= nums[j]

        print(prefix)
        print(posfix)
        
        res = []
        for i in range(n):
            res.append(prefix[i] * posfix[i])

        return res



        


        



        




    






