import java.io.IOException;

public class Main {
    // the number is parsed byte by byte from System.in, which needs much less
    // memory than Scanner
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
        // a row ends in white or red; it comes from a row one shorter ending in
        // the other of the two, or from one two shorter followed by blue
        long prev = 2, cur = 2;
        for (int i = 2; i < n; i++) {
            long next = prev + cur;
            prev = cur;
            cur = next;
        }
        System.out.println(cur);
    }
}
