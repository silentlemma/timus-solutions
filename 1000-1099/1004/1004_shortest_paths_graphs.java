import java.io.DataInputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class Main {
    private static final int INF = 1 << 30;
    private static final int END_OF_INPUT = -1;
    private static final int BUFFER_SIZE = 1 << 16;

    private static final DataInputStream IN = new DataInputStream(System.in);
    private static final byte[] BUF = new byte[BUFFER_SIZE];
    private static int bufLen = 0;
    private static int bufPos = 0;

    private static int read() throws IOException {
        if (bufPos == bufLen) {
            bufLen = IN.read(BUF, 0, BUFFER_SIZE);
            bufPos = 0;
            if (bufLen <= 0) {
                return -1;
            }
        }
        return BUF[bufPos++];
    }

    private static int nextInt() throws IOException {
        int c = read();
        while (c != '-' && (c < '0' || c > '9')) {
            c = read();
        }
        boolean negative = c == '-';
        if (negative) {
            c = read();
        }
        int x = 0;
        while (c >= '0' && c <= '9') {
            x = x * 10 + (c - '0');
            c = read();
        }
        return negative ? -x : x;
    }

    public static void main(String[] args) throws IOException {
        PrintWriter out = new PrintWriter(System.out);
        int n;
        while ((n = nextInt()) != END_OF_INPUT) {
            int m = nextInt();
            int[][] edge = new int[n][n]; // the lightest direct road
            int[][] next = new int[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    edge[i][j] = i == j ? 0 : INF;
                    next[i][j] = j;
                }
            }
            for (int e = 0; e < m; e++) {
                int a = nextInt() - 1;
                int b = nextInt() - 1;
                int l = nextInt();
                if (l < edge[a][b]) {
                    edge[a][b] = l;
                    edge[b][a] = l;
                }
            }
            int[][] dist = new int[n][];
            for (int i = 0; i < n; i++) {
                dist[i] = edge[i].clone();
            }

            // Floyd-Warshall; before vertex k becomes an intermediate,
            // dist[i][j] uses only vertices below k: i..j plus j-k-i is a cycle.
            int best = INF;
            List<Integer> cycle = null;
            for (int k = 0; k < n; k++) {
                for (int i = 0; i < k; i++) {
                    if (edge[i][k] == INF) {
                        continue;
                    }
                    for (int j = i + 1; j < k; j++) {
                        if (edge[k][j] == INF || dist[i][j] == INF) {
                            continue;
                        }
                        int c = dist[i][j] + edge[i][k] + edge[k][j];
                        if (c < best) {
                            best = c;
                            cycle = new ArrayList<>();
                            for (int v = i; v != j; v = next[v][j]) {
                                cycle.add(v);
                            }
                            cycle.add(j);
                            cycle.add(k);
                        }
                    }
                }
                for (int i = 0; i < n; i++) {
                    int dik = dist[i][k];
                    if (dik == INF) {
                        continue;
                    }
                    int[] di = dist[i];
                    int[] dk = dist[k];
                    for (int j = 0; j < n; j++) {
                        if (dik + dk[j] < di[j]) {
                            di[j] = dik + dk[j];
                            next[i][j] = next[i][k];
                        }
                    }
                }
            }
            if (cycle == null) {
                out.println("No solution.");
                continue;
            }
            StringBuilder line = new StringBuilder();
            for (int v : cycle) {
                if (line.length() > 0) {
                    line.append(' ');
                }
                line.append(v + 1);
            }
            out.println(line);
        }
        out.flush();
    }
}
