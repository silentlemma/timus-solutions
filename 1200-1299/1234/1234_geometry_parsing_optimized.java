import java.io.IOException;
import java.util.*;

public class Main {
    static final int TENTHS = 10, BRICK_SIDES = 3, HOLE_SIDES = 2;

    // whether a p x q rectangle (p >= q) fits into an a x b one (a >= b); a
    // turned fit (p > a, q <= b) needs ((a+b)/(p+q))^2 + ((a-b)/(p-q))^2 >= 2
    // by Carver's criterion, multiplied out here to stay in integers
    static boolean fits(long p, long q, long a, long b) {
        if (q > b)
            return false;
        if (p <= a)
            return true;
        long s = (p + q) * (p + q), d = (p - q) * (p - q);
        return (a + b) * (a + b) * d + (a - b) * (a - b) * s >= 2 * s * d;
    }

    public static void main(String[] args) throws IOException {
        GoalInput in = new GoalInput();
        long[] brick = new long[BRICK_SIDES], hole = new long[HOLE_SIDES];
        for (int i = 0; i < brick.length; i++)
            brick[i] = in.scaled(TENTHS);
        for (int i = 0; i < hole.length; i++)
            hole[i] = in.scaled(TENTHS);
        Arrays.sort(brick);
        Arrays.sort(hole);
        // the face of the two shorter sides is the easiest to put through
        System.out.println(fits(brick[1], brick[0], hole[1], hole[0]) ? "YES" : "NO");
    }

    // Token conversion uses one reusable byte buffer rather than regex or reader wrappers.
    static final class GoalInput {
        private final byte[] data = new byte[4096];
        private int position, length;
        private String pending;
        double nval;
        String sval;

        int read() throws IOException {
            if (position >= length) {
                length = System.in.read(data);
                position = 0;
                if (length < 0)
                    return -1;
            }
            return data[position++] & 255;
        }

        private int first() throws IOException {
            int c;
            do {
                c = read();
            } while (c >= 0 && c <= ' ');
            return c;
        }

        long nextLong() throws IOException {
            int c = first();
            boolean negative = c == '-';
            if (negative || c == '+')
                c = read();
            long value = 0;
            while (c >= '0' && c <= '9') {
                value = value * 10 + c - '0';
                c = read();
            }
            return negative ? -value : value;
        }

        int nextInt() throws IOException { return (int)nextLong(); }

        String next() throws IOException {
            if (pending != null) {
                String word = pending;
                pending = null;
                return word;
            }
            int c = first();
            if (c < 0)
                return null;
            StringBuilder word = new StringBuilder();
            while (c > ' ') {
                word.append((char)c);
                c = read();
            }
            return word.toString();
        }

        boolean hasNext() throws IOException {
            if (pending == null)
                pending = next();
            return pending != null;
        }

        void nextToken() throws IOException {
            int c = first();
            if ((c >= '0' && c <= '9') || c == '-' || c == '+') {
                boolean negative = c == '-';
                if (negative || c == '+')
                    c = read();
                long value = 0;
                while (c >= '0' && c <= '9') {
                    value = value * 10 + c - '0';
                    c = read();
                }
                nval = negative ? -value : value;
                sval = null;
            } else {
                StringBuilder word = new StringBuilder();
                while (c > ' ') {
                    word.append((char)c);
                    c = read();
                }
                sval = word.toString();
            }
        }

        long scaled(int scale) throws IOException {
            int c = first();
            boolean negative = c == '-';
            if (negative || c == '+')
                c = read();
            long value = 0;
            boolean fraction = false;
            while (c > ' ') {
                if (c == '.')
                    fraction = true;
                else {
                    value = value * 10 + c - '0';
                    if (fraction)
                        scale /= 10;
                }
                c = read();
            }
            value *= scale;
            return negative ? -value : value;
        }
    }
}
