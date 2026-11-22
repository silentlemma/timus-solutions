public class Main {

    // a single small integer is read byte by byte; no scanner or buffer is needed.
    static int next() throws java.io.IOException {
        int c = System.in.read();
        while (c != -1 && c <= ' ')
            c = System.in.read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }

    static final int THREE = 3, FOUR = 4, GROUP_DIGITS = 9, BLOCK_POWER = 18;
    static final int BASE = 1000000000, DECIMAL = 10;

    public static void main(String[] args) throws java.io.IOException {
        int n = next(), threes = n / THREE, rest = n % THREE;
        if (n < FOUR) {
            System.out.write('0' + n);
            System.out.write('\n');
            return;
        }
        if (rest == 1) {
            threes--;
            rest = FOUR;
        }
        // Each factor 3^18 is below BASE, so one block adds at most one limb.
        int[] limbs = new int[n / (THREE * BLOCK_POWER) + 2];
        limbs[0] = Math.max(rest, 1);
        int length = 1;
        while (threes > 0) {
            int block = Math.min(threes, BLOCK_POWER), multiplier = 1;
            threes -= block;
            for (int i = 0; i < block; i++)
                multiplier *= THREE;
            long carry = 0;
            for (int i = 0; i < length; i++) {
                long value = (long)limbs[i] * multiplier + carry;
                limbs[i] = (int)(value % BASE);
                carry = value / BASE;
            }
            if (carry != 0)
                limbs[length++] = (int)carry;
        }
        byte[] answer = new byte[length * GROUP_DIGITS + 1];
        int at = answer.length;
        answer[--at] = '\n';
        for (int i = 0; i < length; i++) {
            int value = limbs[i], digits = 0;
            do {
                answer[--at] = (byte)('0' + value % DECIMAL);
                value /= DECIMAL;
                digits++;
            } while (value > 0 || (i + 1 < length && digits < GROUP_DIGITS));
        }
        System.out.write(answer, at, answer.length - at);
    }
}
