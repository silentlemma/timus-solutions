import java.io.IOException;

public class Main {
    // the numbers are parsed byte by byte from System.in, which needs much
    // less memory than Scanner
    private static int nextInt() throws IOException {
        int c;
        do {
            c = System.in.read();
        } while (c >= 0 && c <= ' ');
        int sign = 1;
        if (c == '-') {
            sign = -1;
            c = System.in.read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value * sign;
    }

    public static void main(String[] args) throws IOException {
        int n = nextInt(), a = nextInt(), b = nextInt();
        // each panel has two sides of A * B square metres
        System.out.println(2 * n * a * b);
    }
}
