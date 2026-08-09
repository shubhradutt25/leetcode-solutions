class Solution(object):
    def compress(self, chars):
        i = 0                
        k = 0    
        while i<len(chars):
            ch=chars[i]
            count=0
            while i<len(chars) and chars[i]==ch:
                i+=1
                count+=1
            chars[k]=ch
            k+=1
            if count>1:
                for c in str(count):
                    chars[k]=c
                    k+=1
        return k
        