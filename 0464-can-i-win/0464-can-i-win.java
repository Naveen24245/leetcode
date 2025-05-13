class Solution {
    public boolean canIWin(int n, int desiredTotal) {
        Boolean[] dp = new Boolean[(1<<n)+5];
        if (desiredTotal == 0) return true;
        if (n*(n+1)/2<desiredTotal) return false;
        return recur(0, desiredTotal, n, dp);
    }
    public boolean recur(int mask, int remaining, int n, Boolean[] dp) {
        if (remaining<=0) return false;
        if (dp[mask]!=null) return dp[mask];
        boolean res = false;
        for (int i = 0; i < n ;i++) {
            if ((mask&(1<<i))==0) {
                int newmask = (mask|(1<<i));
                if (!recur(newmask, remaining - (i+1), n, dp)) res = true;
            }
        }
        return dp[mask] = res;
    }
}