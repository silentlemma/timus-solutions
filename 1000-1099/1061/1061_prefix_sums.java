import java.io.BufferedInputStream;
import java.io.IOException;
import java.io.InputStream;

public class Main {
    static InputStream in = new BufferedInputStream(System.in);

    static int readInt() throws IOException {
        int c = in.read();
        while (c < '0' || c > '9') {
            c = in.read();
        }
        int v = 0;
        for (; c >= '0' && c <= '9'; c = in.read()) {
            v = v * 10 + (c - '0');
        }
        return v;
    }

    public static void main(String[] args) throws IOException {
        int n = readInt(), k = readInt();
        // value[i] and locks[i]: the sum of values and the number of locked
        // buffers among the first i buffers
        long[] value = new long[n + 1];
        int[] locks = new int[n + 1];
        for (int i = 1; i <= n;) {
            int c = in.read();
            if (c == -1) {
                break;
            }
            if (c == '*') {
                locks[i] = locks[i - 1] + 1;
                value[i] = value[i - 1];
            } else if (c >= '0' && c <= '9') {
                locks[i] = locks[i - 1];
                value[i] = value[i - 1] + (c - '0');
            } else {
                continue;
            }
            i++;
        }
        // the windows [l, l + k - 1] without locks; the first cheapest wins
        int best = 0;
        long bestValue = 0;
        for (int l = 1; l + k - 1 <= n; l++) {
            int r = l + k - 1;
            if (locks[r] != locks[l - 1]) {
                continue;
            }
            long v = value[r] - value[l - 1];
            if (best == 0 || v < bestValue) {
                best = l;
                bestValue = v;
            }
        }
        System.out.println(best);
    }
}
