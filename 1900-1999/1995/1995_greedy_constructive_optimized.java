import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public class Main {
    private static final int PERCENT_SCALE = 100;
    private static final int DECIMAL = 10;

    private static int readInt(BufferedInputStream input) throws IOException {
        int ch = input.read();
        while (ch >= 0 && ch <= ' ') {
            ch = input.read();
        }
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = DECIMAL * value + ch - '0';
            ch = input.read();
        }
        return value;
    }

    private static int nextEnd(int end, int size, int percentage) {
        // All positions up to floor(100 * end / p) can use a rank below end.
        return Math.min(size, PERCENT_SCALE * end / percentage + 1);
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int size = readInt(input);
        int kept = readInt(input);
        int percentage = readInt(input);
        int discarded = size - kept;

        long total = 0;
        int start = 0;
        int end = discarded;
        for (int weight = 1; start < size; weight++) {
            total += (long)(end - start) * weight;
            start = end;
            end = nextEnd(end, size, percentage);
        }

        BufferedOutputStream output = new BufferedOutputStream(System.out);
        output.write(Long.toString(total).getBytes(StandardCharsets.US_ASCII));
        output.write('\n');
        start = 0;
        end = discarded;
        for (int weight = 1; start < size; weight++) {
            byte[] digits = Integer.toString(weight).getBytes(StandardCharsets.US_ASCII);
            for (int position = start; position < end; position++) {
                if (position != 0) {
                    output.write(' ');
                }
                output.write(digits);
            }
            start = end;
            end = nextEnd(end, size, percentage);
        }
        output.write('\n');
        output.flush();
    }
}
