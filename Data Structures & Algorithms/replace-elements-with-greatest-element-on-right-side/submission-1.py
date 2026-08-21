class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp_high = -1
        temp = 0
        i = len(arr) - 1
        while(i >= 0):
            if(arr[i] > temp_high):
                temp = arr[i]
                arr[i] = temp_high
                temp_high = temp
            else:
                arr[i] = temp_high
            i -= 1

        return arr
         
        