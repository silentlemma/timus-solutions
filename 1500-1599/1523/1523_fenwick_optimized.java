import java.io.*;
import java.util.Arrays;
public class Main {
    static final int MOD = 1000000000;
    static final int BUFFER_SIZE = 4096;
    static final byte[] input = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position >= available) {
            available = System.in.read(input);
            position = 0;
            if (available < 0)
                return -1;
        }
        return input[position++];
    }

    static int nextInt() throws java.io.IOException {
        int c = read();
        while (c <= ' ')
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }

    public static void main(String[] args) throws Exception {
        int n = nextInt(), k = nextInt();
        if (k > n) {
            System.out.println(0);
            return;
        }
        short[] flipped = new short[n];
        for (int i = 0; i < n; i++)
            flipped[i] = (short)(n + 1 - nextInt());
        int[] ways = new int[n], tree = new int[n + 1];
        Arrays.fill(ways, 1);
        int total = 0;
        for (int length = 2; length <= k; length++) {
            Arrays.fill(tree, 0);
            total = 0;
            boolean nonzero = false;
            for (int i = 0; i < n; i++) {
                int old = ways[i], result = 0;
                for (int j = flipped[i] - 1; j > 0; j &= j - 1) {
                    result += tree[j];
                    if (result >= MOD)
                        result -= MOD;
                }
                ways[i] = result;
                if (result != 0) {
                    nonzero = true;
                    total += result;
                    if (total >= MOD)
                        total -= MOD;
                }
                // The next position needs the old layer, not the new result.
                if (old != 0)
                    for (int j = flipped[i]; j <= n; j += j & -j) {
                        tree[j] += old;
                        if (tree[j] >= MOD)
                            tree[j] -= MOD;
                    }
            }
            if (!nonzero) {
                System.out.println(0);
                return;
            }
        }
        System.out.println(total);
    }
}
