import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String s = in.readLine().trim();
        int n = s.length();
        // dp[j]: fewest palindromes for the prefix of length j. Centres go left
        // to right, so every palindrome s[l..r] meets a final dp[l]: those that
        // end before l have their centres before l.
        int[] dp = new int[n + 1], prev = new int[n + 1];
        Arrays.fill(dp, n + 1);
        dp[0] = 0;
        for (int twice = 0; twice < 2 * n - 1; twice++) {
            int l = twice / 2, r = l + twice % 2;
            while (l >= 0 && r < n && s.charAt(l) == s.charAt(r)) {
                if (dp[l] + 1 < dp[r + 1]) {
                    dp[r + 1] = dp[l] + 1;
                    prev[r + 1] = l;
                }
                l--;
                r++;
            }
        }
        Deque<String> parts = new ArrayDeque<>();
        for (int end = n; end > 0; end = prev[end])
            parts.addFirst(s.substring(prev[end], end));
        System.out.println(dp[n]);
        System.out.println(String.join(" ", parts));
    }
}
