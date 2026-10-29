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
        int first = nextInt(), second = nextInt();
        // on night k the thief tries code k on lock 1 when k is even and on
        // lock 2 when k is odd
        System.out.println(first % 2 == 0 || second % 2 == 1 ? "yes" : "no");
    }
}
