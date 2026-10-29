public class Main {
    public static void main(String[] args) throws java.io.IOException {
        // the number is parsed byte by byte from System.in, which needs much less
        // memory than Scanner
        int c;
        do {
            c = System.in.read();
        } while (c >= 0 && c <= ' ');
        long n = 0;
        while (c >= '0' && c <= '9') {
            n = n * 10 + c - '0';
            c = System.in.read();
        }
        // each number of dots v sits on n + 2 ends: on the tiles v-w for every w,
        // and twice on the double v-v; so the dots add up to (n + 2) * (0 + ... + n)
        System.out.println((n + 2) * n * (n + 1) / 2);
    }
}
