public class Main {
    // the numbers are parsed byte by byte from System.in, which needs much
    // less memory than Scanner
    static int nextInt() throws java.io.IOException {
        int c;
        do {
            c = System.in.read();
        } while (c >= 0 && c <= ' ');
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }

    public static void main(String[] args) throws java.io.IOException {
        long n = nextInt(), k = nextInt();
        // numbers of valid prefixes ending with a zero and with another digit,
        // where the first digit is not zero
        long zero = 0, other = k - 1;
        for (long i = 1; i < n; i++) {
            long nextZero = other;
            other = (zero + other) * (k - 1);
            zero = nextZero;
        }
        System.out.println(zero + other);
    }
}
