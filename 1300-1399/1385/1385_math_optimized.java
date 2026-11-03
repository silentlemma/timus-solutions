import java.io.BufferedOutputStream;
import java.util.Arrays;

public class Main {
    static final int DECIMAL_BASE = 10, PREFIX_PLACES = 3;
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
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }

    public static void main(String[] args) throws Exception {
        int n = nextInt(), places = Math.min(n, PREFIX_PLACES), unit = 1;
        for (int i = 0; i < places; i++)
            unit *= DECIMAL_BASE;
        int count = 0;
        // Divisibility among k<10 stabilizes once the exponent reaches3.
        // Derive the short prefix rather than storing literal answer values.
        for (int k = 1; k < DECIMAL_BASE; k++)
            if (unit % k == 0)
                count += unit / k - unit / DECIMAL_BASE;
        BufferedOutputStream out = new BufferedOutputStream(System.out, BUFFER_SIZE);
        String prefix = Integer.toString(count);
        for (int i = 0; i < prefix.length(); i++)
            out.write(prefix.charAt(i));
        byte[] zeros = new byte[BUFFER_SIZE];
        Arrays.fill(zeros, (byte)'0');
        for (int remaining = n - places; remaining > 0;) {
            int chunk = Math.min(remaining, BUFFER_SIZE);
            out.write(zeros, 0, chunk);
            remaining -= chunk;
        }
        out.write('\n');
        out.flush();
    }
}
