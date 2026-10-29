import java.io.IOException;

public class Main {
    // the numbers are parsed byte by byte from System.in, which needs much
    // less memory than Scanner
    private static long nextLong() throws IOException {
        int c;
        do {
            c = System.in.read();
        } while (c >= 0 && c <= ' ');
        int sign = 1;
        if (c == '-' || c == '+') {
            if (c == '-') {
                sign = -1;
            }
            c = System.in.read();
        }
        // accumulated as a negative number, so the smallest long fits as well
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 - (c - '0');
            c = System.in.read();
        }
        return sign < 0 ? value : -value;
    }

    public static void main(String[] args) throws IOException {
        long a = nextLong(), b = nextLong();
        System.out.println(a + b);
    }
}
