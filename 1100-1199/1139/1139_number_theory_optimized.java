public class Main {
    // the numbers are parsed by hand from System.in: a Scanner alone costs more
    // than a megabyte
    private static long nextLong() throws java.io.IOException {
        int c;
        do {
            c = System.in.read();
        } while (c >= 0 && c <= ' ');
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }

    private static long gcd(long a, long b) {
        while (b != 0) {
            long remainder = a % b;
            a = b;
            b = remainder;
        }
        return a;
    }

    public static void main(String[] args) throws java.io.IOException {
        long n = nextLong(), m = nextLong();
        // an a by b grid: the diagonal crosses a + b - 2 inner lines, two at once
        // at each of the gcd(a, b) - 1 inner corners; it starts in one block and
        // every crossing enters a new one
        long a = n - 1, b = m - 1;
        System.out.println(a + b - gcd(a, b));
    }
}
