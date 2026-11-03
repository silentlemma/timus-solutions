public class Main {
    static final int ROOT = 31623, BUFFER_SIZE = 4096;
    static final int MAX_TESTS = 1000, ROOT_DIGITS = 9, PREFIX_AND_SEPARATORS = 6;
    static final int BASE = 10;
    static final byte[] input = new byte[BUFFER_SIZE];
    static final byte[] output = new byte[MAX_TESTS * (2 * ROOT_DIGITS + PREFIX_AND_SEPARATORS)];
    static int position, available, used;
    static char[] primes;

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
        while (c >= 0 && c <= ' ')
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * BASE + c - '0';
            c = read();
        }
        return value;
    }

    static void buildPrimes() {
        boolean[] composite = new boolean[ROOT + 1];
        for (int i = 2; i * i <= ROOT; i++)
            if (!composite[i])
                for (int j = i * i; j <= ROOT; j += i)
                    composite[j] = true;
        int count = 0;
        for (int i = 2; i <= ROOT; i++)
            if (!composite[i])
                count++;
        primes = new char[count];
        int index = 0;
        for (int i = 2; i <= ROOT; i++)
            if (!composite[i])
                primes[index++] = (char)i;
    }

    static int factor(int n) {
        // Every valid modulus has a prime factor below ROOT; int division
        // suffices for n<1e9. No boxing, cache or speculative Fermat probe.
        for (char prime : primes)
            if (n % prime == 0)
                return prime;
        throw new IllegalArgumentException();
    }

    static long inverse(long a, long modulus) {
        long r0 = modulus, r1 = a % modulus, s0 = 0, s1 = 1;
        while (r1 != 0) {
            long quotient = r0 / r1;
            long remainder = r0 - quotient * r1, coefficient = s0 - quotient * s1;
            r0 = r1;
            r1 = remainder;
            s0 = s1;
            s1 = coefficient;
        }
        return (s0 % modulus + modulus) % modulus;
    }

    static void write(long value) {
        int first = used;
        do {
            output[used++] = (byte)('0' + value % BASE);
            value /= BASE;
        } while (value != 0);
        for (int left = first, right = used - 1; left < right; left++, right--) {
            byte digit = output[left];
            output[left] = output[right];
            output[right] = digit;
        }
    }

    public static void main(String[] args) throws Exception {
        buildPrimes();
        int count = nextInt();
        for (int test = 0; test < count; test++) {
            int n = nextInt(), p = factor(n), q = n / p;
            long x = q * inverse(q, p), y = n + 1L - x;
            if (x > y) {
                long temporary = x;
                x = y;
                y = temporary;
            }
            output[used++] = '0';
            output[used++] = ' ';
            output[used++] = '1';
            output[used++] = ' ';
            write(x);
            output[used++] = ' ';
            write(y);
            output[used++] = '\n';
        }
        System.out.write(output, 0, used);
    }
}
