import java.io.DataInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    static final int BUFFER_SIZE = 1 << 16;
    static DataInputStream in = new DataInputStream(System.in);
    static byte[] buffer = new byte[BUFFER_SIZE];
    static int length;
    static int index;

    static int read() throws IOException {
        if (index == length) {
            length = in.read(buffer, 0, BUFFER_SIZE);
            index = 0;
            if (length <= 0) {
                return -1;
            }
        }
        return buffer[index++];
    }

    // the next token: a sign or a number, as its first byte or its value
    static int sign() throws IOException {
        int c = read();
        while (c != '+' && c != '-') {
            c = read();
        }
        return c;
    }

    static int number() throws IOException {
        int c = read();
        while (c < '0' || c > '9') {
            c = read();
        }
        int v = 0;
        while (c >= '0' && c <= '9') {
            v = v * 10 + (c - '0');
            c = read();
        }
        return v;
    }

    static int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public static void main(String[] args) throws IOException {
        int q = number();
        boolean[] add = new boolean[q];
        int[] xs = new int[q];
        for (int k = 0; k < q; k++) {
            add[k] = sign() == '+';
            xs[k] = number();
        }
        int[] values = xs.clone();
        Arrays.sort(values);
        int size = 1;
        while (size < q) {
            size *= 2;
        }
        // every addition gets its own leaf; an empty leaf holds 0, which
        // does not change a gcd
        int[] tree = new int[2 * size];
        // the leaves holding each value, as linked stacks
        int[] top = new int[q];
        Arrays.fill(top, -1);
        int[] below = new int[q];
        StringBuilder out = new StringBuilder();
        for (int k = 0; k < q; k++) {
            int x = xs[k];
            int id = Arrays.binarySearch(values, x);
            int v;
            int value = 0;
            if (add[k]) {
                below[k] = top[id];
                top[id] = k;
                v = k + size;
                value = x;
            } else {
                v = top[id] + size;
                top[id] = below[top[id]];
            }
            tree[v] = value;
            // once a node keeps its value, so do all above it
            for (v /= 2; v > 0; v /= 2) {
                int g = gcd(tree[2 * v], tree[2 * v + 1]);
                if (tree[v] == g) {
                    break;
                }
                tree[v] = g;
            }
            out.append(tree[1] == 0 ? 1 : tree[1]).append('\n');
        }
        System.out.print(out);
    }
}
