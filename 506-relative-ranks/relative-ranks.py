class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        # Pair scores with original indices and sort descending
        sorted_scores = sorted(enumerate(score), key=lambda x: x[1], reverse=True)
        
        # Initialize result array
        result = [""] * len(score)
        
        # Map sorted ranks to original positions
        for rank, (index, s) in enumerate(sorted_scores):
            if rank == 0:
                result[index] = "Gold Medal"
            elif rank == 1:
                result[index] = "Silver Medal"
            elif rank == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank + 1)
                
        return result
