class Solution(object):
    def maxSubArray(self, nums):
        current_sum=nums[0]
        max_sum=nums[0]
        for num in nums[1:]:
            current_sum=max(num,current_sum+num)
            if current_sum>max_sum:
                max_sum=current_sum
        return max_sum