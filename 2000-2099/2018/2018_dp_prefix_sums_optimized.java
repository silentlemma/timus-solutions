import java.io.IOException;

public class Main {
    static final long MOD = 1000000007L;
    static final int BUFFER_SIZE = 1024;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, length;

    // the three numbers are parsed by hand from 1 KB blocks, lighter than Scanner
    static int read() throws IOException {
        if (position == length) {
            length = System.in.read(buffer);
            position = 0;
            if (length <= 0)
                return -1;
        }
        return buffer[position++];
    }

    static int nextInt() throws IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        boolean negative = c == '-';
        if (negative)
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return negative ? -value : value;
    }

    // only the last a + 1 values ending in two and b + 1 ending in one are kept,
    // in circular buffers; the two window sums move one step per length
    static long solve(int n, int a, int b) {
        long[] endsOne = new long[b + 1];
        long[] endsTwo = new long[a + 1];
        endsOne[0] = endsTwo[0] = 1;
        long windowOne = 1, windowTwo = 1, lastOne = 0, lastTwo = 0;
        for (int length = 1; length <= n; length++) {
            lastOne = windowOne;
            lastTwo = windowTwo;
            long expiredTwo = length >= a ? endsTwo[(length - a) % (a + 1)] : 0;
            long expiredOne = length >= b ? endsOne[(length - b) % (b + 1)] : 0;
            windowOne = (windowOne + lastTwo + MOD - expiredTwo) % MOD;
            windowTwo = (windowTwo + lastOne + MOD - expiredOne) % MOD;
            endsOne[length % (b + 1)] = lastOne;
            endsTwo[length % (a + 1)] = lastTwo;
        }
        return (lastOne + lastTwo) % MOD;
    }

    public static void main(String[] args) throws IOException {
        int n = nextInt(), a = nextInt(), b = nextInt();
        System.out.println(solve(n, a, b));
    }
}
