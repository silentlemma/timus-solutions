import java.io.IOException;
import java.io.InputStream;

public class Main {
    private static final int BUFFER_SIZE = 65536;
    private static final InputStream INPUT = System.in;
    private static final byte[] BUFFER = new byte[BUFFER_SIZE];
    private static int position;
    private static int length;

    private static int read() throws IOException {
        if (position == length) {
            length = INPUT.read(BUFFER);
            position = 0;
            if (length < 0) {
                return -1;
            }
        }
        return BUFFER[position++];
    }

    private static int nextInt() throws IOException {
        int current = read();
        while (current <= ' ') {
            current = read();
        }
        int value = 0;
        while (current >= '0' && current <= '9') {
            value = value * 10 + current - '0';
            current = read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        int levels = nextInt();
        int queries = nextInt();
        int count = 1 << levels;
        long[] prefix = new long[count + 1];
        for (int index = 0; index < count; index++) {
            prefix[index + 1] = prefix[index] + nextInt();
        }

        long[][] elapsed = new long[levels + 1][];
        elapsed[0] = new long[count];
        int half = 1;
        for (int level = 1; level <= levels; level++) {
            int starts = count - 2 * half + 1;
            long[] previous = elapsed[level - 1];
            long[] current = new long[starts];
            for (int left = 0; left < starts; left++) {
                long difference = 2 * prefix[left + half] - prefix[left];
                difference -= prefix[left + 2 * half];
                // A merge starts when both halves have finished mixing.
                current[left] = Math.max(previous[left], previous[left + half]);
                current[left] += Math.abs(difference);
            }
            elapsed[level] = current;
            half *= 2;
        }

        StringBuilder output = new StringBuilder();
        for (int query = 0; query < queries; query++) {
            int left = nextInt() - 1;
            int level = nextInt();
            output.append(elapsed[level][left]).append(".0\n");
        }
        System.out.print(output);
    }
}
