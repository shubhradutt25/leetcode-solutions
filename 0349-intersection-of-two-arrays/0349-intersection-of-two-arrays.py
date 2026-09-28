class Solution(object):
    def intersection(self, nums1, nums2):
        lookup_set = set(nums1)
        result = []
        
        # Check elements of nums2 against the set
        for num in nums2:
            if num in lookup_set:
                result.append(num)
                # Remove the element to prevent adding duplicates to the result
                lookup_set.remove(num)
                
        return result
