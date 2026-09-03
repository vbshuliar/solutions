from math import prod 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(len(nums)):
            if i == 0:
                out.append(prod(nums[1:]))
            elif i == len(nums)-1:
                out.append(prod(nums[:-1]))
            else:
                out.append(prod(nums[:i])*prod(nums[i+1:])) 
        return out
        