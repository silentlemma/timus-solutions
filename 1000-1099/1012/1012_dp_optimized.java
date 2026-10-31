public class Main {
    static final int MAX_SUM = 1800, LIMB_DIGITS = 9;
    static final long BASE = 1000000000;

    // refillable storage keeps input memory constant, regardless of input length.
    static final int BUFFER_SIZE = 4096;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int at, size;
    static int read() throws java.io.IOException {
        if (at == size) {
            size = System.in.read(buffer);
            at = 0;
            if (size < 0)
                return -1;
        }
        return buffer[at++];
    }
    static long nextLong() throws java.io.IOException {
        int c;
        do {
            c = read();
        } while (c >= 0 && c <= ' ');
        boolean negative = c == '-';
        if (negative)
            c = read();
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return negative ? -value : value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = (int)nextLong(), k = (int)nextLong();
        // the answer is below 10^n and n < 1800; one extra limb handles every carry.
        long[] zero = new long[MAX_SUM / LIMB_DIGITS + 1], other = new long[zero.length];
        // numbers of valid prefixes ending with a zero and with another digit,
        // where the first digit is not zero.
        other[0] = k - 1;
        int used = 1;
        for (int i = 1; i < n; i++) {
            long carry = 0;
            for (int j = 0; j < used; j++) {
                // k <= 10 keeps the product and carry below 18 * base, within long.
                long next = (zero[j] + other[j]) * (k - 1) + carry;
                zero[j] = other[j];
                other[j] = next % BASE;
                carry = next / BASE;
            }
            if (carry != 0)
                other[used++] = carry;
        }
        long carry = 0;
        for (int j = 0; j < used; j++) {
            long next = zero[j] + other[j] + carry;
            other[j] = next % BASE;
            carry = next / BASE;
        }
        if (carry != 0)
            other[used++] = carry;
        StringBuilder out = new StringBuilder().append(other[used - 1]);
        for (int j = used - 2; j >= 0; j--) {
            String limb = Long.toString(other[j]);
            for (int pad = limb.length(); pad < LIMB_DIGITS; pad++)
                out.append('0');
            out.append(limb);
        }
        System.out.println(out);
    }
}
