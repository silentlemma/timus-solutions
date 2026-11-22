public class Main {
    static final int WORD_BITS = 64, HALF_BITS = 32, DECIMAL = 10, INPUT_SIZE = 64;
    static final long HALF_MASK = (1L << HALF_BITS) - 1, SIGN_BIT = 1L << (WORD_BITS - 1);
    static long carry(long previous, long sum) {
        return (sum ^ SIGN_BIT) < (previous ^ SIGN_BIT) ? 1 : 0;
    }
    static long timesTenHigh(long low, long high) {
        long lower = (low & HALF_MASK) * DECIMAL;
        long upper = (low >>> HALF_BITS) * DECIMAL + (lower >>> HALF_BITS);
        return high * DECIMAL + (upper >>> HALF_BITS);
    }
    static byte[] build(int n) {
        byte[] digits = new byte[n + 1];
        long low = 0, high = 0, powerLow = 1, powerHigh = 0;
        for (int k = 0; k < n; k++) {
            long word = k < WORD_BITS ? low : high;
            int bit = k < WORD_BITS ? k : k - WORD_BITS;
            int digit = ((word >>> bit) & 1) == 0 ? 2 : 1;
            digits[n - 1 - k] = (byte)('0' + digit);
            for (int count = 0; count < digit; count++) {
                long sum = low + powerLow;
                high += powerHigh + carry(low, sum);
                low = sum;
            }
            powerHigh = timesTenHigh(powerLow, powerHigh);
            powerLow *= DECIMAL;
        }
        digits[n] = '\n';
        return digits;
    }
    public static void main(String[] args) throws java.io.IOException {
        byte[] input = new byte[INPUT_SIZE];
        int n = 0, size;
        boolean started = false;
        while ((size = System.in.read(input)) >= 0) {
            for (int i = 0; i < size; i++) {
                int c = input[i];
                if (c >= '0' && c <= '9') {
                    n = n * DECIMAL + c - '0';
                    started = true;
                } else if (started) {
                    System.out.write(build(n));
                    return;
                }
            }
        }
        System.out.write(build(n));
    }
}
