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
    static long nextLong() throws java.io.IOException {
        int c;
        do {
            c = read();
        } while (c >= 0 && c <= ' ');
        int sign = 1;
        if (c == '-') {
            sign = -1;
            c = read();
        }
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value * sign;
    }

    private static final int TARGET = 20;
    private static final long BOUND = 2000000; // trial divisors; then at most two primes remain

    public static void main(String[] args) throws java.io.IOException {
        long n = nextLong();
        int count = 0;
        long d = 2;
        for (; d <= BOUND && d * d <= n; d++) {
            while (n % d == 0) {
                n /= d;
                count++;
            }
        }
        if (n > 1) {
            // what is left is prime; otherwise n >= BOUND^2, the divided part is at
            // most 10^18 / BOUND^2, fewer than 18 factors, and the rest adds at most two
            count = d * d > n ? count + 1 : -1;
        }
        System.out.println(count == TARGET ? "Yes" : "No");
    }
}
