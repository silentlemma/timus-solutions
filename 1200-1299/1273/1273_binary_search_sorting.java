import java.io.*;
import java.util.Arrays;

public class Main {
    static class Input {
        private static final int BUFFER_SIZE = 256, BYTE_MASK = 255;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position, length;
        private int read() throws IOException {
            if (position == length) {
                length = System.in.read(buffer);
                position = 0;
                if (length <= 0)
                    return -1;
            }
            return buffer[position++] & BYTE_MASK;
        }
        int number() throws IOException {
            int c = read();
            while (c >= 0 && c <= ' ')
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
    }

    static final int OFFSET = 1000, FIELD_BITS = 11, MASK = (1 << FIELD_BITS) - 1;
    public static void main(String[] args) throws IOException {
        Input in = new Input();
        int n = in.number();
        int[] sleepers = new int[n], tails = new int[n];
        for (int i = 0; i < n; ++i) {
            int left = in.number(), right = in.number();
            // Each shifted coordinate is in 0..2000 and fits eleven bits.
            sleepers[i] = (left + OFFSET) << FIELD_BITS | (right + OFFSET);
        }
        Arrays.sort(sleepers);
        int kept = 0;
        for (int sleeper : sleepers) {
            int right = (sleeper & MASK) - OFFSET;
            int low = 0, high = kept;
            while (low < high) {
                int middle = (low + high) / 2;
                if (tails[middle] < right)
                    low = middle + 1;
                else
                    high = middle;
            }
            tails[low] = right;
            if (low == kept)
                ++kept;
        }
        System.out.println(n - kept);
    }
}
