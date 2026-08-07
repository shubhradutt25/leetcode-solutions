class Solution(object):
    def largestEven(self, s):
        last_two = s.rfind('2')
        
        if last_two == -1:
            return ""
        
        return s[:last_two + 1]