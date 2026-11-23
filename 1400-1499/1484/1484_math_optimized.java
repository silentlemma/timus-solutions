import java.io.IOException;

public class Main {
    static final long TOP = 10;    // the highest vote
    static final long HALVES = 20; // a rating counts in half tenths

    static long tenths(String s) {
        int dot = s.indexOf('.');
        String whole = dot < 0 ? s : s.substring(0, dot);
        String part = dot < 0 ? "0" : s.substring(dot + 1) + "0";
        return Long.parseLong(whole) * 10 + (part.charAt(0) - '0');
    }

    public static void main(String[] args) throws IOException {
        FastInput in = new FastInput();
        long x = tenths(in.next()), y = tenths(in.next()), n = in.nextLong();
        // n votes from 1 to 10 show x when (2x - 1) n <= 20 sum < (2x + 1) n,
        // and the worst case is the largest such sum, and there may be none at all
        long total = Math.min(TOP * n, ((2 * x + 1) * n - 1) / HALVES);
        long least = Math.max(n, ((2 * x - 1) * n + HALVES - 1) / HALVES);
        // k votes of 1 show at most y when 20 (total + k) < (2y + 1)(n + k)
        long excess = HALVES * total - (2 * y + 1) * n, step = 2 * y + 1 - HALVES;
        if (least > total || (excess >= 0 && step <= 0))
            System.out.println("Impossible");
        else if (excess < 0)
            System.out.println(0);
        else
            System.out.println(excess / step + 1);
    }

    // A bounded byte buffer avoids Scanner's regex machinery and temporary tokens.
    static final class FastInput {
        private final byte[] buffer = new byte[4096];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = System.in.read(buffer);
                position = 0;
                if (length < 0)
                    return -1;
            }
            return buffer[position++];
        }

        long nextLong() throws IOException {
            int c;
            do {
                c = read();
            } while (c >= 0 && c <= ' ');
            boolean negative = c == '-';
            if (negative)
                c = read();
            long value = 0;
            while (c >= '0' && c <= '9') {
                value = value * 10 + c - '0';
                c = read();
            }
            return negative ? -value : value;
        }

        String next() throws IOException {
            int c;
            do {
                c = read();
            } while (c >= 0 && c <= ' ');
            StringBuilder word = new StringBuilder();
            while (c > ' ') {
                word.append((char)c);
                c = read();
            }
            return word.toString();
        }
    }
}
