# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        rows = []
        element = []
        for i in range(numRows):
            for j in range(i+1):
                element.append(self.factorial(i)//(self.factorial(j)*self.factorial(i-j)))
            rows.append(element)
            element = []

        return(rows)

    def factorial(self,n):
            if n==0:
                return 1
            else:
                return (self.factorial(n-1)*n)
