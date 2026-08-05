class Solution(object):
    def majorityElement(self, nums):
        count={}
        for n in nums:
            if n in count:
                count[n]+=1
            else:
                count[n]=1
            if count[n]> len(nums)/2:
                return n