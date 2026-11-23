import java.io.IOException;
import java.util.Arrays;

public class Main {
    static final int INPUT_BUFFER_BYTES = 4096;
    // times in units of 1/50 s: a car (20 km/h) covers a metre in 9 units and
    // Egor (5 km/h) crosses a 2 m lane in 72
    static final int METRE = 9;
    static final int LANE = 72;
    static final int CAR = 5;
    static final double UNITS = 50;
    static final long MICROSECONDS_PER_UNIT = 20000;
    static final long LOW_WORD_MASK = 0xffffffffL;

    public static void main(String[] args) throws IOException {
        GoalInput in = new GoalInput();
        long[] blocked = new long[0];
        // a car is on the crossing from METRE d to METRE (d + CAR); a start time
        // s is bad when Egor's time in the car's lane overlaps that
        for (int lane = 0; lane < 2; lane++) {
            int count = in.nextInt();
            long[] more = Arrays.copyOf(blocked, blocked.length + count);
            for (int i = 0; i < count; i++) {
                int d = in.nextInt();
                int enter = lane * LANE;
                int left = METRE * d - enter - LANE;
                int right = METRE * (d + CAR) - enter;
                // Signed left endpoints sort in the high word;
                // the low word stores the right endpoint.
                more[blocked.length + i] = ((long)left << 32) | (right & LOW_WORD_MASK);
            }
            blocked = more;
        }
        Arrays.sort(blocked);
        int start = 0;
        for (long b : blocked) {
            if ((int)(b >> 32) >= start) {
                break;
            }
            start = Math.max(start, (int)b);
        }
        fixed(MICROSECONDS_PER_UNIT * start, 6);
    }

    // Token conversion uses one reusable byte buffer rather than regex or reader wrappers.
    static final class GoalInput {
        private final byte[] data = new byte[INPUT_BUFFER_BYTES];
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

    // Write an already rounded fixed-point value without temporary decimal strings.
    static void fixed(long value, int places) {
        byte[] output = new byte[40];
        int position = output.length;
        output[--position] = '\n';
        for (int i = 0; i < places; i++) {
            output[--position] = (byte)('0' + value % 10);
            value /= 10;
        }
        output[--position] = '.';
        do {
            output[--position] = (byte)('0' + value % 10);
            value /= 10;
        } while (value != 0);
        System.out.write(output, position, output.length - position);
    }
}
