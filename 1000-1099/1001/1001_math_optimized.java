import java.io.BufferedOutputStream;
import java.io.IOException;

public class Main {
    private static final int MAX_INPUT = 256 * 1024;
    private static final int SCALE = 10000;
    private static final int LINE_BYTES = 24;
    private static final int DECIMAL_PLACES = 4;
    private static final double ROUNDING_OFFSET = 0.5;

    public static void main(String[] args) throws IOException {
        byte[] input = new byte[MAX_INPUT];
        int end = 0;
        while (end < input.length) {
            int count = System.in.read(input, end, input.length - end);
            if (count < 0) {
                break;
            }
            end += count;
        }
        BufferedOutputStream out = new BufferedOutputStream(System.out);
        byte[] line = new byte[LINE_BYTES];
        // the numbers are parsed from the end of the input backwards, so they
        // come out in the required order without an array of them
        while (end > 0) {
            while (end > 0 && input[end - 1] <= ' ') {
                end--;
            }
            int start = end;
            while (start > 0 && input[start - 1] > ' ') {
                start--;
            }
            if (start == end) {
                break;
            }
            long value = 0;
            for (int i = start; i < end; i++) {
                value = value * 10 + input[i] - '0';
            }
            // four decimals by hand: the root times 10^4, rounded, written digit
            // by digit from the end of the line; String.format is far slower
            long scaled = (long)(Math.sqrt(value) * SCALE + ROUNDING_OFFSET);
            int position = line.length;
            line[--position] = '\n';
            for (int i = 0; i < DECIMAL_PLACES; i++) {
                line[--position] = (byte)('0' + scaled % 10);
                scaled /= 10;
            }
            line[--position] = '.';
            do {
                line[--position] = (byte)('0' + scaled % 10);
                scaled /= 10;
            } while (scaled > 0);
            out.write(line, position, line.length - position);
            end = start;
        }
        out.flush();
    }
}
