class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Track the top three distinct maximums initialized to negative infinity
        first = second = third = float('-inf')
        
        for num in nums:
            # Skip duplicates to ensure distinct counts
            if num == first or num == second or num == third:
                continue
                
            # Shift the maximums down as we find larger numbers
            if num > first:
                first, second, third = num, first, second
            elif num > second:
                second, third = num, second
            elif num > third:
                third = num
                
        # If the third maximum was never updated, return the highest maximum
        return third if third != float('-inf') else first
