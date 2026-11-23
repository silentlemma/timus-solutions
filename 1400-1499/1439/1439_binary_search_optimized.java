import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        GoalInput in = new GoalInput();
        in.nextLong();
        int m = in.nextInt();
        long[] gone = new long[m]; // original numbers of destroyed rooms, sorted
        int count = 0;
        GoalOutput out = new GoalOutput();
        for (int i = 0; i < m; i++) {
            char letter = in.next().charAt(0);
            long x = in.nextLong();
            // gone[j] - j <= x holds for a prefix: the rooms gone below room x
            int lo = 0, hi = count;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (gone[mid] - mid <= x)
                    lo = mid + 1;
                else
                    hi = mid;
            }
            long original = x + lo;
            if (letter == 'D') {
                System.arraycopy(gone, lo, gone, lo + 1, count - lo);
                gone[lo] = original;
                count++;
            } else {
                out.number(original);
            }
        }
        out.flush();
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

    static final class GoalOutput {
        private final byte[] buffer = new byte[8192];
        private final byte[] digits = new byte[20];
        private int length;
        void number(long value) throws IOException {
            int start = digits.length;
            do {
                digits[--start] = (byte)('0' + value % 10);
                value /= 10;
            } while (value != 0);
            if (length + digits.length - start + 1 > buffer.length)
                flush();
            while (start < digits.length)
                buffer[length++] = digits[start++];
            buffer[length++] = '\n';
        }
        void flush() throws IOException {
            System.out.write(buffer, 0, length);
            length = 0;
        }
    }
}
