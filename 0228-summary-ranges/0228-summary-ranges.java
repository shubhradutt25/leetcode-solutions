import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> ranges = new ArrayList<>();
        if (nums == null || nums.length == 0) {
            return ranges;
        }
        
        int i = 0;
        while (i < nums.length) {
            int start = nums[i];
            while (i + 1 < nums.length && nums[i + 1] == nums[i] + 1) {
                i++;
            }
            
            // Format the range based on whether it is a single number or a true range
            if (start == nums[i]) {
                ranges.add(String.valueOf(start));
            } else {
                ranges.add(start + "->" + nums[i]);
            }
            
            // Move to the next potential range start
            i++;
        }
        
        return ranges;
    }
}
