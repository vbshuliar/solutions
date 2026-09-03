from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        suf = []
        for i in range(len(nums)):
            pref.append(prod(nums[:i]))
            suf.append(prod(nums[i+1:]))
        return [a * b for a, b in zip(pref, suf)]


    
    