class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        temp = 0
        i = 0
        while i < len(nums):
            if(nums[i] == 1):
                temp +=1
            else:
                count = max(count,temp)
                temp = 0
            
            i += 1         
        count = max(count,temp)
        return count


            
        