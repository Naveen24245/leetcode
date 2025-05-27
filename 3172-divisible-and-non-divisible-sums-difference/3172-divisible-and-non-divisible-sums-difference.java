public class Solution {
    public int differenceOfSums(int n, int m) {
        int totalSum = n * (n + 1) / 2;
        int k = n / m;
        int divisibleSum = m * k * (k + 1) / 2;
        return totalSum - 2 * divisibleSum;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.differenceOfSums(10, 3)); // 19
        System.out.println(sol.differenceOfSums(5, 6));  // 15
        System.out.println(sol.differenceOfSums(5, 1));  // -15
    }
}
