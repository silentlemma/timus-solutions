import java.io.*;
import java.util.*;

public class Main {
    static final int BASE = 10;
    static final int INF = 1 << 30;

    // digit i of s from the lowest, zero past its length
    static int digit(String s, int i) {
        return i < s.length() ? s.charAt(s.length() - 1 - i) - '0' : 0;
    }

    // the lowest digit position i may take: the first digit may not become zero
    static int least(String s, int i) { return i == s.length() - 1 ? 1 : 0; }

    // the highest: past its own length a number has only the digit 0
    static int most(String s, int i) { return i < s.length() ? BASE - 1 : 0; }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String s; (s = br.readLine()) != null;)
            all.append(s).append(' ');
        StringTokenizer st = new StringTokenizer(all.toString());
        String a = st.nextToken(), b = st.nextToken(), c = st.nextToken();
        int width = c.length();
        if (Math.max(a.length(), b.length()) > width) {
            System.out.println(-1); // the sum would be longer than C
            return;
        }
        // cost[carry]: the cheapest fix of the lower positions that carries this
        int[] cost = {0, INF};
        for (int i = 0; i < width; i++) {
            int[] next = {INF, INF};
            for (int carry = 0; carry < 2; carry++) {
                if (cost[carry] == INF)
                    continue;
                for (int x = least(a, i); x <= most(a, i); x++)
                    for (int y = least(b, i); y <= most(b, i); y++) {
                        int total = x + y + carry, z = total % BASE;
                        if (z < least(c, i))
                            continue;
                        int v = cost[carry] + Math.abs(x - digit(a, i)) +
                                Math.abs(y - digit(b, i)) + Math.abs(z - digit(c, i));
                        next[total / BASE] = Math.min(next[total / BASE], v);
                    }
            }
            cost = next;
        }
        System.out.println(cost[0] < INF ? cost[0] : -1);
    }
}
