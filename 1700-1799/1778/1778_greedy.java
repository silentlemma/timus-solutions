import java.io.DataInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        Reader in = new Reader();
        int n = in.nextInt(), m = in.nextInt(), a = in.nextInt(), b = in.nextInt();
        int r = in.nextInt(), s = in.nextInt();
        // bus i takes the fans after the border P(i-1) up to the border P(i), with
        // P(0) = 0, P(m) = n and a <= P(i) - P(i-1) <= b; a fan in bus f puts
        // P(f) at or above them and P(f-1) below them
        int[] lo = new int[m + 1], hi = new int[m + 1];
        Arrays.fill(hi, n);
        hi[0] = 0;
        lo[m] = n;
        for (int i = 0; i < s; i++) {
            int fan = in.nextInt(), bus = in.nextInt();
            lo[bus] = Math.max(lo[bus], fan);
            hi[bus - 1] = Math.min(hi[bus - 1], fan - 1);
        }
        // the borders reachable from the left end and from the right end each
        // form a range, and a border is possible when it is in both
        for (int i = 1; i <= m; i++) {
            lo[i] = Math.max(lo[i], lo[i - 1] + a);
            hi[i] = Math.min(hi[i], hi[i - 1] + b);
        }
        for (int i = m - 1; i >= 0; i--) {
            lo[i] = Math.max(lo[i], lo[i + 1] - b);
            hi[i] = Math.min(hi[i], hi[i + 1] - a);
        }
        for (int i = 0; i <= m; i++) {
            if (lo[i] > hi[i]) {
                System.out.println("IMPOSSIBLE");
                return;
            }
        }
        // fan r rides in bus k when some P(k-1) below r and P(k) at or above r
        // are possible borders a to b apart
        StringBuilder list = new StringBuilder();
        int count = 0;
        for (int k = 1; k <= m; k++) {
            int xLo = lo[k - 1], xHi = Math.min(hi[k - 1], r - 1);
            int yLo = Math.max(lo[k], r), yHi = hi[k];
            if (xLo <= xHi && yLo <= yHi && yHi - xLo >= a && yLo - xHi <= b) {
                list.append(count++ > 0 ? " " : "").append(k);
            }
        }
        System.out.println(count + "\n" + list);
    }

    static class Reader {
        private static final int SIZE = 1 << 16;
        private final DataInputStream stream = new DataInputStream(System.in);
        private final byte[] buffer = new byte[SIZE];
        private int length, pointer;

        private int read() throws IOException {
            if (pointer == length) {
                length = stream.read(buffer, 0, SIZE);
                pointer = 0;
                if (length <= 0) return -1;
            }
            return buffer[pointer++];
        }

        int nextInt() throws IOException {
            int c = read();
            while (c != -1 && (c < '0' || c > '9')) c = read();
            int x = 0;
            while (c >= '0' && c <= '9') {
                x = x * 10 + (c - '0');
                c = read();
            }
            return x;
        }
    }
}
