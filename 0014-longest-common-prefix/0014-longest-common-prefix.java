public class Solution {
    public static String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";

        String prefix = strs[0];

        for (int i = 1; i < strs.length; i++) {
            while (!strs[i].startsWith(prefix)) {
                prefix = prefix.substring(0, prefix.length() - 1);
                if (prefix.isEmpty()) return "";
            }
        }

        return prefix;
    }

    public static void main(String[] args) {
        String[] example1 = {"flower", "flow", "flight"};
        System.out.println("Example 1 Output: " + longestCommonPrefix(example1));

        String[] example2 = {"dog", "racecar", "car"};
        System.out.println("Example 2 Output: " + longestCommonPrefix(example2));
    }
}
