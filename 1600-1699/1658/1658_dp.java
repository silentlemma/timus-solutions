import java.io.*;

public class Main {
    static final int LONGEST = 100, TOP = 9; // digits allowed in the answer, largest digit
    static final int S1 = LONGEST * TOP, S2 = LONGEST * TOP * TOP;
    static final int NONE = 255;

    public static void main(String[] args) throws IOException {
        // fewest[s1][s2]: the fewest nonzero digits with these sums, NONE if
        // more than 100 are needed or none will do
        byte[] fewest = new byte[(S1 + 1) * (S2 + 1)];
        java.util.Arrays.fill(fewest, (byte)NONE);
        fewest[0] = 0;
        for (int s1 = 1; s1 <= S1; s1++)
            for (int s2 = 1; s2 <= S2; s2++) {
                int best = NONE;
                for (int d = 1; d <= TOP && d <= s1 && d * d <= s2; d++) {
                    int v = (fewest[(s1 - d) * (S2 + 1) + s2 - d * d] & NONE) + 1;
                    if (v < best)
                        best = v;
                }
                if (best <= LONGEST)
                    fewest[s1 * (S2 + 1) + s2] = (byte)best;
            }
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int t = (int)in.nval;
        StringBuilder sb = new StringBuilder();
        while (t-- > 0) {
            in.nextToken();
            int s1 = (int)in.nval;
            in.nextToken();
            int s2 = (int)in.nval;
            if (s1 > S1 || s2 > S2 || (fewest[s1 * (S2 + 1) + s2] & NONE) == NONE) {
                sb.append("No solution\n");
                continue;
            }
            // the smallest digit first that still leaves a way to finish; the
            // digits come out sorted, so each search starts at the last one
            int d = 1;
            for (int left = (fewest[s1 * (S2 + 1) + s2] & NONE) - 1; left >= 0; left--) {
                while (d * d > s2 || d > s1
                       || (fewest[(s1 - d) * (S2 + 1) + s2 - d * d] & NONE) != left)
                    d++;
                sb.append((char)('0' + d));
                s1 -= d;
                s2 -= d * d;
            }
            sb.append('\n');
        }
        System.out.print(sb);
    }
}
