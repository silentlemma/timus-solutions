import java.io.BufferedOutputStream;
import java.util.Arrays;

public class Main {
    static final int MAX_COORD = 1000;
    static final int MAX_DENOMINATOR = 4 * MAX_COORD;
    static final long SCALE = (long)MAX_DENOMINATOR * MAX_DENOMINATOR;
    static final long HALF_TURN = 2 * SCALE, FULL_TURN = 4 * SCALE;
    static final int DISTANCE_BITS = 12, ID_BITS = 15, KEY_SHIFT = DISTANCE_BITS + ID_BITS;
    static final long ID_MASK = (1L << ID_BITS) - 1;
    static final int DECIMAL_BASE = 10;
    static final int BUFFER_SIZE = 4096;
    static final byte[] input = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(input);
            position = 0;
            if (available < 0)
                return -1;
        }
        return input[position++];
    }

    static int nextInt() throws java.io.IOException {
        int c = read();
        while (c <= ' ')
            c = read();
        int sign = 1;
        if (c == '-') {
            sign = -1;
            c = read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return sign * value;
    }

    static final byte[] digits = new byte[Integer.SIZE];
    static BufferedOutputStream out;

    static void writeInt(int value) throws java.io.IOException {
        int at = digits.length;
        do {
            digits[--at] = (byte)('0' + value % DECIMAL_BASE);
            value /= DECIMAL_BASE;
        } while (value > 0);
        out.write(digits, at, digits.length - at);
        out.write('\n');
    }

    public static void main(String[] args) throws Exception {
        int n = nextInt(), ox = nextInt(), oy = nextInt();
        long[] keys = new long[n - 1];
        for (int identity = 2; identity <= n; identity++) {
            int dx = nextInt() - ox, dy = nextInt() - oy, distance = Math.abs(dx) + Math.abs(dy);
            long rank = dy > 0 || (dy == 0 && dx > 0)
                            ? (distance - (long)dx) * SCALE / distance
                            : HALF_TURN + (distance + (long)dx) * SCALE / distance;
            keys[identity - 2] = (rank << KEY_SHIFT) | ((long)distance << ID_BITS) | identity;
        }
        Arrays.sort(keys);
        int start = 0;
        long previous = keys[keys.length - 1] >>> KEY_SHIFT;
        for (int i = 0; i < keys.length; i++) {
            long current = keys[i] >>> KEY_SHIFT, gap = current - previous;
            if (gap < 0)
                gap += FULL_TURN;
            if (gap >= HALF_TURN)
                start = i;
            previous = current;
        }
        out = new BufferedOutputStream(System.out, BUFFER_SIZE);
        writeInt(n);
        writeInt(1);
        for (int i = start; i < keys.length; i++)
            writeInt((int)(keys[i] & ID_MASK));
        for (int i = 0; i < start; i++)
            writeInt((int)(keys[i] & ID_MASK));
        out.flush();
    }
}
