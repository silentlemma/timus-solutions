public class Main {
    // the numbers are parsed byte by byte from System.in, which needs much
    // less memory than Scanner
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

    public static void main(String[] args) throws java.io.IOException {
        long n = nextLong(), k = nextLong();
        // as long as fewer computers than cables have the program, each hour doubles
        // the count; after that k computers get it each hour
        long have = 1, hours = 0;
        while (have < n && have < k) {
            have *= 2;
            hours++;
        }
        if (have < n) {
            hours += (n - have + k - 1) / k;
        }
        System.out.println(hours);
    }
}
