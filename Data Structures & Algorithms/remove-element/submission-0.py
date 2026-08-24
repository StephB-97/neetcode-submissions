class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        tmp = 0
        for num in range(len(nums)):
            if nums[num] != val:
                nums[tmp] = nums[num]
                tmp += 1
                k += 1
            
        

        return k    
            
