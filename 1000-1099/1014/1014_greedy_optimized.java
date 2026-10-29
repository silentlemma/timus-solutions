public class Main {
    static final int BASE = 10;

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
        int n = nextInt();
        // a zero digit makes the product zero: 10 is the smallest such number
        if (n == 0) {
            System.out.println(BASE);
            return;
        }
        if (n == 1) {
            System.out.println(1);
            return;
        }
        // the largest digits first give the fewest digits; then sort them up
        // the digits are appended and the string is reversed once at the end,
        // instead of inserting each digit at the front
        StringBuilder digits = new StringBuilder();
        for (int d = BASE - 1; d >= 2; d--) {
            while (n % d == 0) {
                digits.append(d);
                n /= d;
            }
        }
        System.out.println(n == 1 ? digits.reverse().toString() : "-1");
    }
}
