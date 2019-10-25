class Solution:
    '''
    Time: O(N) iterates once through the array
    Space: O(N) generates a dictionary
    '''

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary that holds index and value of nums
        solution = {}

        for i, value in enumerate(nums):
            rem = target - value

            if rem not in solution:
                # Unless the remainder is already in the dictionary put the current value
                # and index into the solution dictionary
                solution[value] = i
            else:
                # returns the index of the remainder and current index in the for loop
                return [solution[remainder], i]
