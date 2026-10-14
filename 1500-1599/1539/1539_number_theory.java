import java.io.*;
import java.util.*;

public class Main {
    static final int BASE = 10;

    // the decimal text times 10^d, as an integer
    static long scaled(String text, int d) {
        int dot = text.indexOf('.');
        String whole = dot < 0 ? text : text.substring(0, dot),
               frac = dot < 0 ? "" : text.substring(dot + 1);
        long v = 0;
        for (char c : whole.toCharArray())
            v = v * BASE + (c - '0');
        for (int i = 0; i < d; i++)
            v = v * BASE + (i < frac.length() ? frac.charAt(i) - '0' : 0);
        return v;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        List<String> tokens = new ArrayList<>();
        for (String line; (line = in.readLine()) != null;)
            for (StringTokenizer st = new StringTokenizer(line); st.hasMoreTokens();)
                tokens.add(st.nextToken());
        int d = Integer.parseInt(tokens.get(0)), n = Integer.parseInt(tokens.get(1));
        long one = 1;
        for (int i = 0; i < d; i++)
            one *= BASE;
        // only the fractional parts matter, and a whole number fits any group
        List<Long> values = new ArrayList<>();
        Set<Long> seen = new HashSet<>(Collections.singleton(0L));
        for (int i = 0; i < n; i++) {
            long v = scaled(tokens.get(2 + i), d) % one;
            if (seen.add(v))
                values.add(v);
        }
        long den = 2 * one;
        // an average v (times 10^d) over q goblins comes from a total p when
        // (2v - 1) q <= den p < (2v + 1) q; q = 10^d always works, as the
        // interval is then at least 1 long
        for (long q = 1; q <= one; q++) {
            boolean fits = true;
            for (int i = 0; i < values.size(); i++) {
                long v = values.get(i);
                long low = ((2 * v - 1) * q + den - 1) / den; // the smallest total allowed
                if (low * den >= (2 * v + 1) * q) {
                    // the average that failed is likely to fail again: try it first
                    values.add(0, values.remove(i));
                    fits = false;
                    break;
                }
            }
            if (fits) {
                System.out.println(q);
                return;
            }
        }
    }
}
