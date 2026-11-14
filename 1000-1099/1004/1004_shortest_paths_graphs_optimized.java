import java.io.BufferedInputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Arrays;

public class Main {
    private static final short INF = Short.MAX_VALUE;
    private static final int MIN_CYCLE_LENGTH = 3;

    private static int number(BufferedInputStream input) throws IOException {
        int c = input.read();
        while (c >= 0 && c <= ' ') {
            c = input.read();
        }
        if (c == '-' || c < 0) {
            return -1;
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = 10 * value + c - '0';
            c = input.read();
        }
        return value;
    }

    private static void solve(int n, BufferedInputStream input, PrintWriter output)
        throws IOException {
        short[][] direct = new short[n][n];
        byte[][] next = new byte[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(direct[i], INF);
            direct[i][i] = 0;
            for (int j = 0; j < n; j++) {
                next[i][j] = (byte)j;
            }
        }
        int roads = number(input);
        for (int i = 0; i < roads; i++) {
            int a = number(input) - 1, b = number(input) - 1;
            short length = (short)number(input);
            if (length < direct[a][b]) {
                direct[a][b] = direct[b][a] = length;
            }
        }
        short[][] distance = new short[n][];
        for (int i = 0; i < n; i++) {
            distance[i] = direct[i].clone();
        }

        int best = INF, count = 0;
        int[] cycle = new int[n];
    search:
        for (int k = 0; k < n; k++) {
            short[] roadsFromK = direct[k];
            for (int i = 0; i < k; i++) {
                int left = roadsFromK[i];
                if (left >= best) {
                    continue;
                }
                for (int j = i + 1; j < k; j++) {
                    int length = left + roadsFromK[j] + distance[i][j];
                    if (length < best) {
                        best = length;
                        count = 0;
                        for (int v = i; v != j; v = next[v][j]) {
                            cycle[count++] = v;
                        }
                        cycle[count++] = j;
                        cycle[count++] = k;
                        if (best == MIN_CYCLE_LENGTH) {
                            break search;
                        }
                    }
                }
            }
            short[] middle = distance[k];
            for (int i = 0; i < n; i++) {
                int left = middle[i];
                if (i == k || left >= best) {
                    continue;
                }
                short[] row = distance[i];
                byte[] hop = next[i];
                for (int j = i + 1; j < n; j++) {
                    int length = left + middle[j];
                    if (length < best && length < row[j]) {
                        row[j] = distance[j][i] = (short)length;
                        hop[j] = hop[k];
                        next[j][i] = next[j][k];
                    }
                }
            }
        }
        if (count == 0) {
            output.println("No solution.");
        } else {
            StringBuilder line = new StringBuilder();
            line.append(cycle[0] + 1);
            for (int i = 1; i < count; i++) {
                line.append(' ').append(cycle[i] + 1);
            }
            output.println(line);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        PrintWriter output = new PrintWriter(System.out);
        for (int n = number(input); n > 0; n = number(input)) {
            solve(n, input, output);
        }
        output.flush();
    }
}
