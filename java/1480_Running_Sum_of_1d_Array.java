class Solution {
    public int[] runningSum(int[] nums) {
        if (nums.length <= 1) return nums;
        int accu = nums[0];
        for (int i = 1; i < nums.length; i++) {
            accu += nums[i];
            nums[i] = accu;
        }
        return nums;
    }
}
