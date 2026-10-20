import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int TRIANGLE_SIZE = 3;
    private static final BufferedInputStream INPUT = new BufferedInputStream(System.in);

    private static int nextInt() throws IOException {
        int current = INPUT.read();
        while (current <= ' ' && current >= 0) {
            current = INPUT.read();
        }
        int value = 0;
        while (current >= '0' && current <= '9') {
            value = value * 10 + current - '0';
            current = INPUT.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        int n = nextInt();
        boolean[][] adj = new boolean[n][n];
        for (int u = 0; u < n; u++) {
            for (int v = 0; v < n; v++) {
                adj[u][v] = nextInt() == 1;
            }
        }

        boolean[] used = new boolean[n];
        int[][] pairs = new int[n / 2][2];
        int pairCount = 0;
        for (int u = 0; u < n; u++) {
            if (used[u]) {
                continue;
            }
            for (int v = 0; v < n; v++) {
                if (!used[v] && adj[u][v]) {
                    used[u] = true;
                    used[v] = true;
                    pairs[pairCount][0] = u;
                    pairs[pairCount][1] = v;
                    pairCount++;
                    break;
                }
            }
        }

        int[] unmatched = new int[n];
        int unmatchedCount = 0;
        for (int u = 0; u < n; u++) {
            if (!used[u]) {
                unmatched[unmatchedCount++] = u;
            }
        }
        for (int i = 0; i + 1 < unmatchedCount; i += 2) {
            int u = unmatched[i];
            int v = unmatched[i + 1];
            // Two unmatched vertices always admit an augmentation through one pair.
            for (int j = 0; j < pairCount; j++) {
                int a = pairs[j][0];
                int b = pairs[j][1];
                if (adj[u][a] && adj[v][b]) {
                    pairs[j][0] = u;
                    pairs[j][1] = a;
                    pairs[pairCount][0] = v;
                    pairs[pairCount][1] = b;
                    pairCount++;
                    break;
                }
                if (adj[u][b] && adj[v][a]) {
                    pairs[j][0] = u;
                    pairs[j][1] = b;
                    pairs[pairCount][0] = v;
                    pairs[pairCount][1] = a;
                    pairCount++;
                    break;
                }
            }
        }

        int triangle = -1;
        int extra = -1;
        if (unmatchedCount % 2 == 1) {
            extra = unmatched[unmatchedCount - 1];
            for (int i = 0; i < pairCount; i++) {
                if (adj[extra][pairs[i][0]] && adj[extra][pairs[i][1]]) {
                    triangle = i;
                    break;
                }
            }
        }

        StringBuilder output = new StringBuilder();
        output.append("YES\n").append(pairCount).append('\n');
        for (int i = 0; i < pairCount; i++) {
            output.append(i == triangle ? TRIANGLE_SIZE : 2);
            output.append(' ').append(pairs[i][0] + 1);
            output.append(' ').append(pairs[i][1] + 1);
            if (i == triangle) {
                output.append(' ').append(extra + 1);
            }
            output.append('\n');
        }
        System.out.print(output);
    }
}
