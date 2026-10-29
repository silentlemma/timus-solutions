import java.io.IOException;

public class Main {
    // the numbers are parsed byte by byte from System.in, which needs much
    // less memory than Scanner
    private static int readInt() throws IOException {
        int c;
        do {
            c = System.in.read();
        } while (c <= ' ' && c != -1);
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int k = readInt();
        // every minute fries at most k of the 2n sides, and one steak takes
        // two minutes on its own; rotating sides cyclically reaches both bounds
        System.out.println(Math.max(2, (2 * n + k - 1) / k));
    }
}
