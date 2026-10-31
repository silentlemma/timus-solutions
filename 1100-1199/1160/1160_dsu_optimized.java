import java.io.IOException;
import java.util.Arrays;

public class Main {

    // refilling this buffer bounds input storage independently of input size.
    static final int INPUT_BUFFER = 4096;
    static final byte[] buffer = new byte[INPUT_BUFFER];
    static int pos, len;

    static int read() throws IOException {
        if (pos == len) {
            len = System.in.read(buffer);
            pos = 0;
            if (len <= 0)
                return -1;
        }
        return buffer[pos++];
    }

    static int next() throws IOException {
        int c = read();
        while (c != -1 && c <= ' ')
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }

    static final int HUB_BITS = 10, LENGTH_BITS = 2 * HUB_BITS;
    static final int HUB_MASK = (1 << HUB_BITS) - 1;
    static int[] parent;
    static int find(int v) {
        while (parent[v] != v)
            v = parent[v] = parent[parent[v]];
        return v;
    }
    public static void main(String[] args) throws IOException {
        int n = next(), m = next();
        // n <= 1000 uses ten bits per hub; length <= 10^6 needs twenty more.
        long[] edges = new long[m];
        for (int i = 0; i < m; i++) {
            int a = next(), b = next(), length = next();
            edges[i] = ((long)length << LENGTH_BITS) | (a << HUB_BITS) | b;
        }
        Arrays.sort(edges);
        parent = new int[n + 1];
        for (int i = 1; i <= n; i++)
            parent[i] = i;
        int count = 0, longest = 0;
        StringBuilder plan = new StringBuilder();
        for (long e : edges) {
            int a = (int)(e >> HUB_BITS) & HUB_MASK, b = (int)e & HUB_MASK;
            int ra = find(a), rb = find(b);
            if (ra != rb) {
                parent[ra] = rb;
                longest = (int)(e >> LENGTH_BITS);
                plan.append(a).append(' ').append(b).append('\n');
                if (++count == n - 1)
                    break;
            }
        }
        System.out.println(longest);
        System.out.println(count);
        System.out.print(plan);
    }
}
