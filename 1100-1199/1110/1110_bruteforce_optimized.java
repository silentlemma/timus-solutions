public class Main {
    // the three numbers are parsed by hand from System.in: a Scanner alone costs
    // more than a megabyte
    private static int nextInt() throws java.io.IOException {
        int ch;
        do {
            ch = System.in.read();
        } while (ch >= 0 && ch <= ' ');
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * 10 + ch - '0';
            ch = System.in.read();
        }
        return value;
    }

    // x^exponent mod modulus by repeated squaring
    private static int power(int x, int exponent, int modulus) {
        int result = 1;
        for (; exponent > 0; exponent >>= 1) {
            if ((exponent & 1) == 1) {
                result = result * x % modulus;
            }
            x = x * x % modulus;
        }
        return result;
    }

    static final int DECIMAL = 10, DIGITS = 3;

    static boolean[] findRoots(int exponent, int modulus, int remainder) {
        boolean[] roots = new boolean[modulus];
        if (remainder < modulus) {
            roots[0] = remainder == 0;
            // Each pair x and M-x needs only one modular exponentiation.
            for (int x = 1; x <= modulus / 2; x++) {
                int value = power(x, exponent, modulus);
                roots[x] = value == remainder;
                int opposite = (exponent & 1) == 0 || value == 0 ? value : modulus - value;
                roots[modulus - x] = opposite == remainder;
            }
        }
        return roots;
    }

    public static void main(String[] args) throws java.io.IOException {
        int exponent = nextInt(), modulus = nextInt(), remainder = nextInt();
        boolean[] roots = findRoots(exponent, modulus, remainder);
        byte[] answer = new byte[(DIGITS + 1) * modulus], digits = new byte[DIGITS];
        int length = 0;
        for (int x = 0; x < modulus; x++) {
            if (!roots[x])
                continue;
            if (length > 0)
                answer[length++] = ' ';
            int value = x, count = 0;
            do {
                digits[count++] = (byte)('0' + value % DECIMAL);
                value /= DECIMAL;
            } while (value > 0);
            while (count > 0)
                answer[length++] = digits[--count];
        }
        if (length == 0) {
            answer[length++] = '-';
            answer[length++] = '1';
        }
        answer[length++] = '\n';
        System.out.write(answer, 0, length);
    }
}
