import java.io.IOException;

public class Main {
    private static final long LIMIT = 1000000000L; // the largest absolute mood

    private static long[] a;
    private static long smallest = LIMIT;

    private static boolean possible(long x) {
        // Every mood below x must be flipped, so the shortest segment covers them
        // all, and every mood inside must become at least x.
        int first = -1;
        int last = -1;
        for (int i = 0; i < a.length; i++) {
            if (a[i] < x) {
                if (first < 0)
                    first = i;
                last = i;
            }
        }
        if (first < 0)
            return smallest <= -x; // some single mood can still be flipped
        for (int i = first; i <= last; i++) {
            if (a[i] > -x)
                return false;
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        GoalInput in = new GoalInput();
        in.nextToken();
        int n = (int)in.nval;
        a = new long[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            a[i] = (long)in.nval;
            smallest = Math.min(smallest, a[i]);
        }
        long lo = -LIMIT;
        long hi = LIMIT;
        while (lo < hi) {
            long middle = lo + (hi - lo + 1) / 2;
            if (possible(middle)) {
                lo = middle;
            } else {
                hi = middle - 1;
            }
        }
        System.out.println(lo);
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
