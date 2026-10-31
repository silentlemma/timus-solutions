public class Main {

    // these inputs contain only nonnegative integers; avoid scanner's regex machinery.
    static long nextLong() throws java.io.IOException {
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
        long n = nextLong();
        // (n^2)^2 = n^4 = n^3 * n
        System.out.println(n * n);
        System.out.println(n);
    }
}
