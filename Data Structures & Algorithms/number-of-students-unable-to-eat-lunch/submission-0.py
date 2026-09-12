class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        onesCount = 0
        zerosCount = 0

        for i in students:
            if i == 0:
                zerosCount += 1
            else:
                onesCount += 1

        for j in sandwiches:
            if j == 1 and onesCount != 0:
                onesCount -= 1
            elif j == 0 and zerosCount != 0:
                zerosCount -= 1
            else:
                break
        return (onesCount + zerosCount)

        