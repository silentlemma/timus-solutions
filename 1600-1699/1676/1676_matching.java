import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int m;
    static boolean[][] beats; // beats[i][j] when fighter j beats monster i
    static int[] owner;
    static int[] match;
    static boolean[] seen;

    // Kuhn's augmenting search from monster u
    static boolean augment(int u) {
        for (int j = 0; j < m; j++) {
            if (beats[u][j] && !seen[j]) {
                seen[j] = true;
                if (owner[j] < 0 || augment(owner[j])) {
                    owner[j] = u;
                    match[u] = j;
                    return true;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            text.append(line).append(' ');
        }
        StringTokenizer words = new StringTokenizer(text.toString());
        n = Integer.parseInt(words.nextToken());
        m = Integer.parseInt(words.nextToken());
        StringBuilder cells = new StringBuilder();
        while (cells.length() < n * m && words.hasMoreTokens()) {
            cells.append(words.nextToken());
        }
        beats = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                beats[i][j] = cells.charAt(i * m + j) == '1';
            }
        }
        owner = new int[m];
        match = new int[n];
        java.util.Arrays.fill(owner, -1);
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++) {
            seen = new boolean[m];
            if (!augment(i)) {
                // some monster cannot be beaten in any assignment
                StringBuilder row = new StringBuilder();
                for (int j = 0; j < m; j++) {
                    row.append('1');
                }
                for (int k = 0; k < n; k++) {
                    out.append(row).append('\n');
                }
                System.out.print(out);
                return;
            }
        }
        // i may take fighter j if j is free or its own, or if j's monster k moves on:
        // with k -> k2 when k can take k2's fighter, k reaches i (closing a cycle)
        // or reaches a monster (k included) that some free fighter beats
        List<List<Integer>> next = new ArrayList<>();
        boolean[] loose = new boolean[n];
        for (int k = 0; k < n; k++) {
            next.add(new ArrayList<>());
            for (int j = 0; j < m; j++) {
                if (beats[k][j]) {
                    if (owner[j] < 0) {
                        loose[k] = true;
                    } else if (owner[j] != k) {
                        next.get(k).add(owner[j]);
                    }
                }
            }
        }
        boolean[][] reach = new boolean[n][n];
        boolean[] helped = new boolean[n];
        int[] queue = new int[n + 1];
        for (int k = 0; k < n; k++) {
            int tail = 0;
            queue[tail++] = k;
            for (int h = 0; h < tail; h++) {
                for (int k2 : next.get(queue[h])) {
                    if (!reach[k][k2]) {
                        reach[k][k2] = true;
                        queue[tail++] = k2;
                    }
                }
            }
            helped[k] = loose[k];
            for (int x = 0; x < n; x++) {
                helped[k] = helped[k] || reach[k][x] && loose[x];
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                boolean ok = beats[i][j]
                    && (owner[j] < 0 || match[i] == j || helped[owner[j]] || reach[owner[j]][i]);
                out.append(ok ? '0' : '1');
            }
            out.append('\n');
        }
        System.out.print(out);
    }
}
