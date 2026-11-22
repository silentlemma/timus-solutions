import java.io.IOException;
import java.util.Arrays;

public class Main {
    static final int BUFFER_SIZE = 4096, BYTE_MASK = 255;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(buffer);
            position = 0;
            if (available < 0)
                return -1;
        }
        return buffer[position++] & BYTE_MASK;
    }
    static long nextLong() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = 10 * value + c - '0';
            c = read();
        }
        return value;
    }

    private static final int DISPLAY_WIDTH = 17;
    private static final int SECONDS = 60;
    private static final int TENS_VALUES = SECONDS / 10;
    private static final int LINE_WIDTH = 6;
    private static final int WIDTH = 3;
    private static final int[] COLUMNS = {0, 4, 10, 14};
    // Each bit indicates a lit cell in the corresponding 3-by-3 glyph.
    private static final int[] GLYPHS = {490, 288, 242, 434, 312, 410, 474, 290, 506, 442};

    private static long pairMask(int tens, int units) {
        long unitMask = 0;
        for (int digit = 0; digit < GLYPHS.length; digit++) {
            if ((units & GLYPHS[digit]) == units)
                unitMask |= 1L << digit;
        }
        long mask = 0;
        for (int digit = 0; digit < TENS_VALUES; digit++) {
            if ((tens & GLYPHS[digit]) == tens)
                mask |= unitMask << (10 * digit);
        }
        return mask;
    }

    private static int largest(long mask) {
        return Long.SIZE - 1 - Long.numberOfLeadingZeros(mask);
    }

    private static int largestAtMost(long mask, int bound) {
        return largest(mask & ((1L << (bound + 1)) - 1));
    }

    public static void main(String[] args) throws IOException {
        int count = (int)nextLong();
        byte[] output = new byte[count * LINE_WIDTH];
        int used = 0;
        int[] lit = new int[COLUMNS.length];

        int bound = SECONDS * SECONDS - 1;
        for (int reading = 0; reading < count; reading++) {
            Arrays.fill(lit, 0);
            for (int row = 0; row < WIDTH; row++) {
                byte[] line = new byte[DISPLAY_WIDTH];
                int c = read();
                while (c >= 0 && c <= ' ')
                    c = read();
                for (int column = 0; column < line.length; column++) {
                    line[column] = (byte)c;
                    c = read();
                }
                for (int digit = 0; digit < COLUMNS.length; digit++) {
                    int start = COLUMNS[digit];
                    for (int cell = 0; cell < WIDTH; cell++) {
                        if (line[start + cell] != '.')
                            lit[digit] |= 1 << (row * WIDTH + cell);
                    }
                }
            }
            long minutes = pairMask(lit[0], lit[1]);
            long secondMask = pairMask(lit[2], lit[COLUMNS.length - 1]);
            // Take the largest feasible time so every smaller time remains available.
            int minute = bound / SECONDS;
            int second = largestAtMost(secondMask, bound % SECONDS);
            if ((minutes & (1L << minute)) == 0 || second < 0) {
                minute = largestAtMost(minutes, minute - 1);
                second = largest(secondMask);
            }
            output[used++] = (byte)('0' + minute / 10);
            output[used++] = (byte)('0' + minute % 10);
            output[used++] = ':';
            output[used++] = (byte)('0' + second / 10);
            output[used++] = (byte)('0' + second % 10);
            output[used++] = '\n';
            bound = minute * SECONDS + second - 1;
        }
        System.out.write(output, 0, used);
        System.out.flush();
    }
}
