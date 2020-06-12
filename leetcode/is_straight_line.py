# DESCRIPTION
# You are given an array coordinates, coordinates[i] = [x, y],
# where [x, y] represents the coordinate of a point.
# Check if these points make a straight line in the XY plane.

# EXAMPLE 1:
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true

# EXAMPLE 2:
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false

class Solution:
    '''
    Time: O(N), must iterate over every point in the line
    Space: O(1), no extra data structures used
    '''

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        # look for the slope between any two points
        # Collinearity because need to check for vertical lines
        # dy = y1 - y0
        # dx = x1 - x0
        dy = coordinates[1][1] - coordinates[0][1]
        dx = coordinates[1][0] - coordinates[0][0]

        # constant check of the current slope and the
        # first two points
        # dy    yi - y0
        # -- = ---------
        # dx    xi - x0

        # cross multiplying and grouping like terms
        # dx*yi - dy*xi = dx*y0 - dy*x0
        xp = dx*coordinates[0][1] - dy*coordinates[0][0]

        for i in range(2, len(coordinates)):
            # if the slopes are differnt then not a line
            if dx*coordinates[i][1] - dy*coordinates[i][0] != xp:
                return False

        return True
