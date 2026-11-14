import java.io.BufferedInputStream;
import java.io.IOException;
import java.io.OutputStream;

public class Main {
    private static final int PERCENT = 100;
    private static final int PERIODS_PER_BLOCK = 80;

    private static int number(BufferedInputStream input) throws IOException {
        int c = input.read();
        while (c >= 0 && c <= ' ') {
            c = input.read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = input.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int remaining = number(input);
        int brightness = number(input);
        byte[] block = new byte[PERCENT * PERIODS_PER_BLOCK];
        int remainder = 0;
        for (int i = 0; i < PERCENT; i++) {
            remainder += brightness;
            if (remainder >= PERCENT) {
                block[i] = '1';
                remainder -= PERCENT;
            } else {
                block[i] = '0';
            }
        }
        // Repeat the period to fill a fixed-size output block.
        for (int length = PERCENT; length < block.length;) {
            int copied = Math.min(length, block.length - length);
            System.arraycopy(block, 0, block, length, copied);
            length += copied;
        }
        OutputStream output = System.out;
        while (remaining >= block.length) {
            output.write(block);
            remaining -= block.length;
        }
        output.write(block, 0, remaining);
        output.write('\n');
        output.flush();
    }
}
