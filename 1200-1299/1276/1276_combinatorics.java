import java.io.*;
import java.util.*;

public class Main {
    static final int MAXC = 64; // binomials needed only up to 41
    static long[][] binom = new long[MAXC][MAXC];

    // ways to put identical items into runs in order, runs may stay empty
    static long spread(int items, int runs) {
        if (runs == 0)
            return items == 0 ? 1 : 0;
        return binom[items + runs - 1][runs - 1];
    }

    static int bit(char c) { return c == 'B' ? 1 : 0; }

    public static void main(String[] args) throws IOException {
        for (int i = 0; i < MAXC; i++) {
            binom[i][0] = 1;
            for (int j = 1; j <= i; j++)
                binom[i][j] = binom[i - 1][j - 1] + binom[i - 1][j];
        }
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line; (line = reader.readLine()) != null;)
            all.append(line).append(' ');
        StringTokenizer in = new StringTokenizer(all.toString());
        int n = Integer.parseInt(in.nextToken()), k = Integer.parseInt(in.nextToken());
        String loco = in.nextToken();
        int[][] have = new int[2][2]; // have[x][y]: carriages with couplings x, y (0 = A)
        for (int i = 0; i < n; i++) {
            String car = in.nextToken();
            have[bit(car.charAt(0))][bit(car.charAt(1))]++;
        }
        // the train starts with the coupling that fits the locomotive's right
        // end and finishes with the one that fits its left end
        int start = bit(loco.charAt(1)), end = bit(loco.charAt(0));
        long total = 0;
        for (int sw = 0; sw <= k; sw++) {
            // AB and BA carriages must alternate, beginning with the one that
            // leaves the starting coupling
            if ((sw + 1) / 2 > have[start][1 - start] || sw / 2 > have[1 - start][start])
                continue;
            if ((start ^ (sw % 2)) != end)
                continue;
            // the runs between switches hold the AA and BB carriages
            int[] runs = new int[2];
            runs[start] = sw / 2 + 1;
            runs[1 - start] = (sw + 1) / 2;
            for (int aa = 0; aa <= k - sw; aa++) {
                int bb = k - sw - aa;
                if (aa <= have[0][0] && bb <= have[1][1])
                    total += spread(aa, runs[0]) * spread(bb, runs[1]);
            }
        }
        System.out.println(total > 0 ? "YES\n" + total : "NO");
    }
}
