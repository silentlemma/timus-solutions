import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    static final long BASE = 1000000000L;
    static final int LIMB_DIGITS = 9;
    static final int MAX_LIMBS = 334;
    static final int MAX_DIGITS = 3001;
    static final int INPUT_SIZE = 1024;
    static final int DECIMAL_BASE = 10;
    static final int FIRST_PAIR = 4;

    static int scale(int[] limbs, int used, long factor, long offset) {
        long carry = -offset;
        for (int i = 0; i < used; i++) {
            long value = limbs[i] * factor + carry;
            limbs[i] = (int)(value % BASE);
            carry = value / BASE;
        }
        if (carry != 0)
            limbs[used++] = (int)carry;
        return used;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in, INPUT_SIZE);
        int c = input.read();
        while (c >= 0 && c <= ' ')
            c = input.read();
        int n = 0;
        while (c >= '0' && c <= '9') {
            n = n * DECIMAL_BASE + c - '0';
            c = input.read();
        }
        int[] limbs = new int[MAX_LIMBS];
        int used = 1;
        if (n > 1)
            limbs[0] = 1;
        for (int k = FIRST_PAIR; k <= n; k += 2)
            used = scale(limbs, used, k * (k - 1), k - 1);
        if (n > 1 && n % 2 != 0)
            used = scale(limbs, used, n, 1);
        byte[] output = new byte[MAX_DIGITS];
        byte[] digits = new byte[LIMB_DIGITS];
        int written = 0;
        for (int i = used - 1; i >= 0; i--) {
            int count = 0, value = limbs[i];
            do {
                digits[count++] = (byte)('0' + value % DECIMAL_BASE);
                value /= DECIMAL_BASE;
            } while (value != 0);
            if (i != used - 1)
                for (int j = count; j < LIMB_DIGITS; j++)
                    output[written++] = '0';
            while (count != 0)
                output[written++] = digits[--count];
        }
        output[written++] = '\n';
        System.out.write(output, 0, written);
    }
}
