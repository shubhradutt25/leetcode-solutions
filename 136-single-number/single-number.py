class Solution(object):
    def singleNumber(self, nums):
        count={}
        for n in nums:
            if n in count:
                count[n]+=1
            else:
                count[n]=1
        for n in count:
            if count[n]==1:
                return n

#class Solution(object):
   # def singleNumber(self, nums):
        #ans = 0
        #for n in nums:
            #ans ^= n
        #return ans