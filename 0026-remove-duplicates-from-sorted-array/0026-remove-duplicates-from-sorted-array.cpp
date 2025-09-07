class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;

        int a = 1;
        for (int i = 1; i < n; i++) {
            if (nums[i] != nums[a - 1]) { 
                nums[a] = nums[i]; 
                a++;
            }
        }
        return a;
    }
};
