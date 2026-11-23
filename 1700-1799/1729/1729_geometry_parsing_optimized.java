import java.io.IOException;

public class Main {
    private static final int DECIMAL = 10;
    private static final int INPUT_SCALE = 1000;
    private static final int HALF_TURN = 180 * INPUT_SCALE;
    private static final int OUTPUT_SCALE = 10000000;

    private static int thousandths() throws IOException {
        int ch = read();
        while (ch >= 0 && ch <= ' ') {
            ch = read();
        }
        int value = 0;
        int scale = INPUT_SCALE;
        boolean fractional = false;
        while (ch > ' ') {
            if (ch == '.') {
                fractional = true;
            } else {
                value = DECIMAL * value + ch - '0';
                if (fractional) {
                    scale /= DECIMAL;
                }
            }
            ch = read();
        }
        return value * scale;
    }

    public static void main(String[] args) throws IOException {
        double radius = thousandths() / (double)INPUT_SCALE;
        int angle = thousandths();
        int fullChords = HALF_TURN / angle - 1;
        int remainder = HALF_TURN % angle;
        double radiansPerUnit = Math.PI / HALF_TURN;
        double distance = radius * (1 + 2 * (fullChords * Math.sin(angle * radiansPerUnit) +
                                             Math.sin(remainder * radiansPerUnit)));
        long rounded = Math.round(distance * OUTPUT_SCALE);
        fixed(rounded, 7);
        System.out.flush();
        System.err.flush();
        Runtime.getRuntime().halt(0);
    }

    // Token conversion uses one reusable byte buffer rather than regex or reader wrappers.
    private static final byte[] data = new byte[128];
    private static int position, length;
    static int read() throws IOException {
        if (position >= length) {
            length = System.in.read(data);
            position = 0;
            if (length < 0)
                return -1;
        }
        return data[position++] & 255;
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
