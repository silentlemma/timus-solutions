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

    public static void main(String[] args) throws java.io.IOException {
        int exponent = nextInt(), modulus = nextInt(), remainder = nextInt();
        StringBuilder roots = new StringBuilder();
        // only M candidates; a Y of M or more is never a remainder
        if (remainder < modulus) {
            for (int x = 0; x < modulus; ++x) {
                if (power(x, exponent, modulus) == remainder) {
                    if (roots.length() > 0) {
                        roots.append(' ');
                    }
                    roots.append(x);
                }
            }
        }
        System.out.println(roots.length() > 0 ? roots.toString() : "-1");
    }
}
