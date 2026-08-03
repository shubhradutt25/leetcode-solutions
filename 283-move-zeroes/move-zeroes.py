class Solution(object):
    def moveZeroes(self, nums):
        i = 0                              # Position to place the next non-zero element
        for j in range(len(nums)):         # Traverse the array
            if nums[j] != 0:               # If the current element is non-zero
                nums[i] = nums[j]          # Copy it to index i
                i += 1                     # Move i to the next position
        while i < len(nums):               # Fill the remaining positions with 0
            nums[i] = 0
            i += 1