public class Solution {
    public int findKthLargest(int[] nums, int k) {
        int start = 0, end = nums.length - 1;
        while (true){
            int res = search(nums, start, end);
            if (res == k - 1)
                return nums[res];
            if (res > k - 1)
                end = res - 1;
            else
                start = res + 1;
        }
    }
        
    private int search(int[] nums, int start, int end){
        int pivot = nums[start], left = start + 1, right = end, temp = 0;
        while (left <= right){
            System.out.printf("%d, %d", left, right);
            if (nums[left] < pivot && nums[right] > pivot){
                temp = nums[left]; nums[left++] = nums[right]; nums[right--] = temp;
            }
            if (nums[left] >= pivot)
                left++;
            if (nums[right] <= pivot)
                right--;
        }
        temp = nums[start]; nums[start] = nums[right]; nums[right] = temp;
        return right;
    }
}
