import java.io.IOException;

public class Main {
    static final long OUTPUT_SCALE = 1000000000;
    public static void main(String[] args) throws IOException {
        long m = nextLong(), n = nextLong();
        // m * n moves close the tour; m + n + 1 of them are diagonal
        long diagonal = m + n + 1;
        double length = m * n + diagonal * (Math.sqrt(2) - 1);
        long rounded = Math.round(length * OUTPUT_SCALE);
        fixed(rounded, 9);
        System.out.flush();
        System.err.flush();
        Runtime.getRuntime().halt(0);
    }

    // A bounded byte buffer avoids Scanner's regex machinery and temporary tokens.
    private static final byte[] buffer = new byte[128];
    private static int position;
    private static int length;

    private static int read() throws IOException {
        if (position >= length) {
            length = System.in.read(buffer);
            position = 0;
            if (length < 0)
                return -1;
        }
        return buffer[position++];
    }

    static long nextLong() throws IOException {
        int c;
        do {
            c = read();
        } while (c >= 0 && c <= ' ');
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
