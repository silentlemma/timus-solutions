import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    static final int TOP = 99999;
    static final int LAST_PARENT = (TOP + 1) / 2;

    // parsing digits directly avoids scanner and token allocations.
    private static int readInt(BufferedInputStream in) throws IOException {
        int c;
        do {
            c = in.read();
        } while (c >= 0 && c <= ' ');
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = in.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        // n < 2^17 bounds every stern value by fibonacci(19) = 4181, fitting 16 bits.
        char[] a = new char[LAST_PARENT + 1], best = new char[TOP + 1];
        a[1] = best[1] = 1;
        for (int i = 2; i <= TOP; i++) {
            char value = (char)(i % 2 == 0 ? a[i / 2] : a[i / 2] + a[i / 2 + 1]);
            // later terms only refer to indices in the first half.
            if (i <= LAST_PARENT) {
                a[i] = value;
            }
            best[i] = (char)Math.max(best[i - 1], value);
        }
        BufferedInputStream in = new BufferedInputStream(System.in);
        StringBuilder out = new StringBuilder();
        while (true) {
            int n = readInt(in);
            if (n == 0) {
                break;
            }
            out.append((int)best[n]).append("\n");
        }
        System.out.print(out);
    }
}
