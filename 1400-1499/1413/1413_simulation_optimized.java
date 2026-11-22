public class Main {
    static final int KEYS = 10, INPUT_SIZE = 4096, OUTPUT_SIZE = 64;
    static final long PART_SCALE = 1000000000L;
    static final long FRACTION_SCALE = PART_SCALE * PART_SCALE;
    // floor(10^18 / sqrt(2)), split to keep every product within a long.
    static final long COEFFICIENT_HIGH = 707106781L, COEFFICIENT_LOW = 186547524L;
    static final int[] DX = {0, -1, 0, 1, -1, 0, 1, -1, 0, 1};
    static final int[] DY = {0, -1, -1, -1, 0, 0, 0, 1, 1, 1};
    static final byte[] output = new byte[OUTPUT_SIZE];
    static int used;

    static void unsigned(long value) {
        int first = used;
        do {
            output[used++] = (byte)('0' + value % 10);
            value /= 10;
        } while (value != 0);
        for (int left = first, right = used - 1; left < right; left++, right--) {
            byte temporary = output[left];
            output[left] = output[right];
            output[right] = temporary;
        }
    }

    static void coordinate(long straight, long diagonal, int delimiter) {
        long high = diagonal * COEFFICIENT_HIGH;
        long whole = straight + Math.floorDiv(high, PART_SCALE);
        long fraction = Math.floorMod(high, PART_SCALE) * PART_SCALE + diagonal * COEFFICIENT_LOW;
        whole += Math.floorDiv(fraction, FRACTION_SCALE);
        fraction = Math.floorMod(fraction, FRACTION_SCALE);
        if (whole < 0) {
            output[used++] = '-';
            whole = -whole;
            if (fraction != 0) {
                whole--;
                fraction = FRACTION_SCALE - fraction;
            }
        }
        unsigned(whole);
        output[used++] = '.';
        for (long divisor = FRACTION_SCALE / 10; divisor != 0; divisor /= 10) {
            output[used++] = (byte)('0' + fraction / divisor);
            fraction %= divisor;
        }
        output[used++] = (byte)delimiter;
    }

    public static void main(String[] args) throws java.io.IOException {
        long[] times = new long[KEYS];
        byte[] input = new byte[INPUT_SIZE];
    scan:
        for (int size; (size = System.in.read(input)) >= 0;) {
            for (int i = 0; i < size; i++) {
                int key = input[i];
                if (key == '0')
                    break scan;
                if (key > '0' && key <= '9')
                    times[key - '0']++;
            }
        }
        long sx = 0, sy = 0, dx = 0, dy = 0;
        for (int key = 0; key < KEYS; key++) {
            if (DX[key] != 0 && DY[key] != 0) {
                dx += DX[key] * times[key];
                dy += DY[key] * times[key];
            } else {
                sx += DX[key] * times[key];
                sy += DY[key] * times[key];
            }
        }
        coordinate(sx, dx, ' ');
        coordinate(sy, dy, '\n');
        System.out.write(output, 0, used);
        System.out.flush();
    }
}
