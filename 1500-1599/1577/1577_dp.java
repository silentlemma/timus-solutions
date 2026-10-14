import java.io.*;
import java.util.*;

public class Main {
    static final int MOD = 1000000007;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        String line;
        while ((line = in.readLine()) != null)
            all.append(line).append(' ');
        StringTokenizer words = new StringTokenizer(all.toString());
        String a = words.nextToken(), b = words.nextToken();
        int n = a.length(), m = b.length();
        // length[j] and count[j]: the shortest common supersequences of a[i:] and
        // b[j:], their length and number; row i needs only row i + 1
        int[] length = new int[m + 1], count = new int[m + 1];
        int[] belowLen = new int[m + 1], belowCnt = new int[m + 1];
        for (int j = 0; j <= m; j++) {
            length[j] = m - j; // i = n: only b[j:] itself
            count[j] = 1;
        }
        for (int i = n - 1; i >= 0; i--) {
            int[] swap = belowLen;
            belowLen = length;
            length = swap;
            swap = belowCnt;
            belowCnt = count;
            count = swap;
            length[m] = n - i; // only a[i:] itself
            count[m] = 1;
            for (int j = m - 1; j >= 0; j--) {
                if (a.charAt(i) == b.charAt(j)) {
                    // the first letter is the common one and covers both
                    length[j] = belowLen[j + 1] + 1;
                    count[j] = belowCnt[j + 1];
                    continue;
                }
                // the first letter is a[i] or b[j]; the two kinds of strings differ
                // in their first letter, so their numbers add up
                int takeA = belowLen[j], takeB = length[j + 1], best = Math.min(takeA, takeB);
                length[j] = best + 1;
                long ways = 0;
                if (takeA == best)
                    ways += belowCnt[j];
                if (takeB == best)
                    ways += count[j + 1];
                count[j] = (int)(ways % MOD);
            }
        }
        System.out.println(count[0]);
    }
}
