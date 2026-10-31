public class Main {

    // refill a small buffer instead of retaining the input or allocating tokens.
    static final int BUFFER_SIZE = 4096;
    static final byte[] BUFFER = new byte[BUFFER_SIZE];
    static int position, length;
    static int read() throws java.io.IOException {
        if (position == length) {
            length = System.in.read(BUFFER);
            position = 0;
            if (length < 0)
                return -1;
        }
        return BUFFER[position++];
    }
    static int nextInt() throws java.io.IOException {
        int c;
        do {
            c = read();
        } while (c >= 0 && c <= ' ');
        int sign = 1;
        if (c == '-') {
            sign = -1;
            c = read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value * sign;
    }

    static final int MOD = 100;
    static final int BASES = 4;
    static final int TEN = 10;

    static int power(int base, int n) {
        int r = 1;
        for (; n > 0; n >>= 1, base = base * base % MOD) {
            if ((n & 1) == 1)
                r = r * base % MOD;
        }
        return r;
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = nextInt();
        // from the second power on the sum is even but never divisible by 8,
        // so it ends in at most two zeros and its remainder mod 100 decides
        int s = 0;
        for (int b = 1; b <= BASES; b++)
            s = (s + power(b, n)) % MOD;
        System.out.println(s == 0 ? 2 : s % TEN == 0 ? 1 : 0);
    }
}
