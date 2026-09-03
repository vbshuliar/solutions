class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def prod(nums):
            res = 1
            for n in nums:
                res *= n
            return res  
        out = []
        for i in range(len(nums)):
            if i == 0:
                out.append(prod(nums[1:]))
            elif i == len(nums)-1:
                out.append(prod(nums[:-1]))
            else:
                out.append(prod(nums[:i])*prod(nums[i+1:])) 
        return out

  

    
    