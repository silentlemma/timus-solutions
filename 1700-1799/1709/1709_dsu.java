import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[] parent;

    static int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        String line;
        while ((line = in.readLine()) != null) {
            all.append(line).append(' ');
        }
        StringTokenizer tokens = new StringTokenizer(all.toString());
        int n = Integer.parseInt(tokens.nextToken());
        long d = Long.parseLong(tokens.nextToken());
        long a = Long.parseLong(tokens.nextToken());
        String[] flights = new String[n];
        for (int i = 0; i < n; i++) {
            flights[i] = tokens.nextToken();
        }
        parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        // the result must be a spanning tree: keep a spanning forest of the
        // existing flights, cancel the rest, then join the trees with new flights
        char[][] plan = new char[n][n];
        for (char[] row : plan) {
            java.util.Arrays.fill(row, '0');
        }
        long cost = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (flights[i].charAt(j) == '1') {
                    int ri = find(i);
                    int rj = find(j);
                    if (ri != rj) {
                        parent[ri] = rj;
                    } else {
                        plan[i][j] = 'd';
                        plan[j][i] = 'd';
                        cost += d;
                    }
                }
            }
        }
        for (int j = 1; j < n; j++) {
            int r0 = find(0);
            int rj = find(j);
            if (r0 != rj) {
                parent[rj] = r0;
                plan[0][j] = 'a';
                plan[j][0] = 'a';
                cost += a;
            }
        }
        StringBuilder out = new StringBuilder();
        out.append(cost).append('\n');
        for (char[] row : plan) {
            out.append(row).append('\n');
        }
        System.out.print(out);
    }
}
