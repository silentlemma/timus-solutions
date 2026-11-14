import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public class Main {
    private static final byte[] ONE = {'1'};

    private static long number(BufferedInputStream input) throws IOException {
        int ch = input.read();
        while (ch >= 0 && ch <= ' ') {
            ch = input.read();
        }
        long value = 0;
        while ('0' <= ch && ch <= '9') {
            value = 10 * value + ch - '0';
            ch = input.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        BufferedOutputStream output = new BufferedOutputStream(System.out);
        int bits = (int)number(input), queries = (int)number(input);
        long[] count = new long[bits + 1];
        long combinations = 1;
        for (int box = 1; box <= bits; ++box) {
            combinations = combinations * (bits - box + 1) / box;
            count[box] = 1 + combinations - (box == 1 ? 1 : 0);
        }
        // Each small box sends its extra bottles to a single smaller box.
        for (int box = bits; box > 1; --box) {
            count[Integer.bitCount(box)] += count[box] - 1;
        }
        byte[][] answers = new byte[bits + 1][];
        for (int box = 1; box <= bits; ++box) {
            answers[box] = Long.toString(count[box]).getBytes(StandardCharsets.US_ASCII);
        }
        for (int i = 0; i < queries; ++i) {
            long box = number(input);
            output.write(box <= bits ? answers[(int)box] : ONE);
            output.write(i + 1 == queries ? '\n' : ' ');
        }
        output.flush();
    }
}
