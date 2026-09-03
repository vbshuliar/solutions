class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pref = [1]
        for i in range(1, len(nums)):
            pref.append(nums[i-1]*pref[i-1])
        
        suf = [1]
        for i in range(-2, -len(nums)-1, -1):
            suf.insert(0,nums[i+1]*suf[i+1])
        
        for i in range(len(pref)):
            pref[i] *= suf[i]

        return pref
 
    