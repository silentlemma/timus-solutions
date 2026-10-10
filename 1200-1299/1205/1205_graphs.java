import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Locale;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tok = new StringTokenizer("");

    static String next() throws IOException {
        while (!tok.hasMoreTokens()) {
            tok = new StringTokenizer(in.readLine());
        }
        return tok.nextToken();
    }

    public static void main(String[] args) throws IOException {
        double walk = Double.parseDouble(next()), metro = Double.parseDouble(next());
        int n = Integer.parseInt(next());
        int total = n + 2, start = n, goal = n + 1;
        double[] x = new double[total], y = new double[total];
        for (int i = 0; i < n; i++) {
            x[i] = Double.parseDouble(next());
            y[i] = Double.parseDouble(next());
        }
        boolean[][] linked = new boolean[total][total];
        while (true) {
            int a = Integer.parseInt(next()), b = Integer.parseInt(next());
            if (a == 0 && b == 0) {
                break;
            }
            linked[a - 1][b - 1] = linked[b - 1][a - 1] = true;
        }
        x[start] = Double.parseDouble(next());
        y[start] = Double.parseDouble(next());
        x[goal] = Double.parseDouble(next());
        y[goal] = Double.parseDouble(next());
        // nodes: the stations, then A and B; the subway is never slower than
        // walking, so a linked pair always goes by train
        double[] dist = new double[total];
        int[] prev = new int[total];
        boolean[] done = new boolean[total];
        Arrays.fill(dist, Double.POSITIVE_INFINITY);
        dist[start] = 0;
        for (int step = 0; step < total; step++) {
            int u = -1;
            for (int v = 0; v < total; v++) {
                if (!done[v] && (u < 0 || dist[v] < dist[u])) {
                    u = v;
                }
            }
            done[u] = true;
            for (int v = 0; v < total; v++) {
                if (!done[v]) {
                    double d = Math.hypot(x[v] - x[u], y[v] - y[u]) / (linked[u][v] ? metro : walk);
                    if (dist[u] + d < dist[v]) {
                        dist[v] = dist[u] + d;
                        prev[v] = u;
                    }
                }
            }
        }
        int[] path = new int[total];
        int len = 0;
        for (int v = prev[goal]; v != start; v = prev[v]) {
            path[len++] = v + 1;
        }
        StringBuilder out = new StringBuilder(String.format(Locale.US, "%.10f", dist[goal]));
        out.append('\n').append(len);
        for (int i = len - 1; i >= 0; i--) {
            out.append(' ').append(path[i]);
        }
        System.out.println(out);
    }
}
