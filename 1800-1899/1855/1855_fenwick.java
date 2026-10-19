import java.io.DataInputStream;
import java.io.IOException;
import java.util.Locale;

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

    // the first letter of the next word, skipping the rest of it
    static int letter() throws IOException {
        int c = read();
        while (c < 'a' || c > 'z') {
            c = read();
        }
        int first = c;
        while (c >= 'a' && c <= 'z') {
            c = read();
        }
        return first;
    }

    static long number() throws IOException {
        int c = read();
        while (c != '-' && (c < '0' || c > '9')) {
            c = read();
        }
        boolean negative = c == '-';
        if (negative) {
            c = read();
        }
        long v = 0;
        while (c >= '0' && c <= '9') {
            v = v * 10 + (c - '0');
            c = read();
        }
        return negative ? -v : v;
    }

    // all sums are kept modulo 2^64: some of them overflow on the way, but
    // the final total of a guild fits in a signed 64-bit number
    static long[] plain;
    static long[] zero;
    static long[] one;
    static long[] two;
    static int size;
    // sums of i and of i^2 for i up to x
    static long[] linear;
    static long[] square;

    static void add(int j, long d) {
        long w0 = d * (j - 1);
        long w1 = d * linear[j - 1];
        long w2 = d * square[j - 1];
        for (; j <= size; j += j & -j) {
            plain[j] += d;
            zero[j] += w0;
            one[j] += w1;
            two[j] += w2;
        }
    }

    // the sums of t_i, i t_i and i^2 t_i over i <= x
    static long[] prefix(int x) {
        long s = 0;
        long s0 = 0;
        long s1 = 0;
        long s2 = 0;
        for (int j = x; j > 0; j -= j & -j) {
            s += plain[j];
            s0 += zero[j];
            s1 += one[j];
            s2 += two[j];
        }
        return new long[] {x * s - s0, linear[x] * s - s1, square[x] * s - s2};
    }

    public static void main(String[] args) throws IOException {
        int n = (int) number();
        int m = (int) number();
        linear = new long[n + 2];
        square = new long[n + 2];
        for (int i = 1; i <= n + 1; i++) {
            linear[i] = linear[i - 1] + i;
            square[i] = square[i - 1] + (long) i * i;
        }
        // toll t_i on segment i (cities i and i + 1) is the prefix sum of
        // the differences dif_j; the sum of i^k t_i over i <= x is
        // S_k(x) * (sum of dif_j) - (sum of dif_j * S_k(j - 1)) over j <= x
        size = n + 1;
        plain = new long[size + 1];
        zero = new long[size + 1];
        one = new long[size + 1];
        two = new long[size + 1];
        StringBuilder out = new StringBuilder();
        for (int e = 0; e < m; e++) {
            int kind = letter();
            int a = (int) number();
            int b = (int) number();
            if (kind == 'c') {
                long d = number();
                add(a, d);
                add(b, -d);
                continue;
            }
            long[] hi = prefix(b - 1);
            long[] lo = prefix(a - 1);
            long s0 = hi[0] - lo[0];
            long s1 = hi[1] - lo[1];
            long s2 = hi[2] - lo[2];
            // segment i lies on (i - a + 1)(b - i) of the guild's routes
            long total = -s2 + (long) (a + b - 1) * s1 + (long) b * (1 - a) * s0;
            long routes = (long) (b - a + 1) * (b - a) / 2;
            out.append(String.format(Locale.US, "%.8f", (double) total / routes)).append('\n');
        }
        System.out.print(out);
    }
}
