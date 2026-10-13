import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
    static int[] x, y;

    static int half(int i) { return y[i] > 0 || (y[i] == 0 && x[i] > 0) ? 0 : 1; }

    static int cross(int i, int j) { return x[i] * y[j] - y[i] * x[j]; }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        x = new int[n];
        y = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            x[i] = (int)in.nval;
            in.nextToken();
            y[i] = (int)in.nval;
        }
        for (int i = n - 1; i >= 0; i--) {
            x[i] -= x[0];
            y[i] -= y[0];
        }
        Integer[] order = new Integer[n - 1];
        for (int i = 1; i < n; i++)
            order[i - 1] = i;
        // by angle around the first pumpkin, nearer first on the same ray
        Arrays.sort(order, (i, j) -> {
            if (half(i) != half(j))
                return half(i) - half(j);
            int c = cross(i, j);
            if (c != 0)
                return -c;
            return Math.abs(x[i]) + Math.abs(y[i]) - Math.abs(x[j]) - Math.abs(y[j]);
        });
        // cut the circle after a turn of at least half a circle, if there is one:
        // then every step turns by less than that and the walk never meets itself
        int m = n - 1, start = 0;
        for (int k = 0; k < m; k++) {
            int a = order[(k + m - 1) % m], b = order[k];
            int c = cross(a, b);
            if (c < 0 || (c == 0 && x[a] * x[b] + y[a] * y[b] < 0))
                start = k;
        }
        StringBuilder out = new StringBuilder();
        out.append(n).append("\n1\n");
        for (int k = 0; k < m; k++)
            out.append(order[(start + k) % m] + 1).append('\n');
        System.out.print(out);
    }
}
