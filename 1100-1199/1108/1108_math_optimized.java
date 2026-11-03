public class Main {
    static final int BASE = 10000;
    static final int DIGITS = 11000;
    static final int DECIMAL_WIDTH = 4;
    static final int OUTPUT_BYTES = 4096;
    static final int[] value = new int[DIGITS];
    static final long[] square = new long[DIGITS];
    static final byte[] output = new byte[OUTPUT_BYTES];
    static int used;

    static void put(int ch) throws java.io.IOException {
        if (used == output.length) {
            System.out.write(output, 0, used);
            used = 0;
        }
        output[used++] = (byte)ch;
    }
    static void emit(int length) throws java.io.IOException {
        int first = value[length - 1], divisor = 1;
        while (divisor * 10 <= first)
            divisor *= 10;
        while (divisor > 0) {
            put('0' + first / divisor);
            first %= divisor;
            divisor /= 10;
        }
        for (int i = length - 2; i >= 0; i--) {
            divisor = BASE / 10;
            for (int j = 0; j < DECIMAL_WIDTH; j++) {
                put('0' + value[i] / divisor % 10);
                divisor /= 10;
            }
        }
        put('\n');
    }
    public static void main(String[] args) throws Exception {
        int n = 0, ch;
        while ((ch = System.in.read()) >= 0)
            if (ch >= '0' && ch <= '9')
                n = n * 10 + ch - '0';
        value[0] = 2;
        int length = 1;
        for (int term = 0; term < n; term++) {
            emit(length);
            if (term + 1 == n)
                break;
            int end = 2 * length;
            for (int i = 0; i < end; i++)
                square[i] = 0;
            for (int i = 0; i < length; i++) {
                square[2 * i] += (long)value[i] * value[i];
                for (int j = i + 1; j < length; j++)
                    square[i + j] += 2L * value[i] * value[j];
            }
            // All old digits are used above before any is overwritten here.
            long carry = 1;
            for (int i = 0; i < end; i++) {
                long total = square[i] + carry - (i < length ? value[i] : 0);
                carry = total / BASE;
                int digit = (int)(total % BASE);
                if (digit < 0) {
                    digit += BASE;
                    carry--;
                }
                value[i] = digit;
            }
            length = end;
            while (value[length - 1] == 0)
                length--;
        }
        System.out.write(output, 0, used);
    }
}
