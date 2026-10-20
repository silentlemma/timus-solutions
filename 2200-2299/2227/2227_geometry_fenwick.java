import java.io.IOException;
import java.io.InputStream;

public class Main {
    private static final int BUFFER_SIZE = 1 << 16;

    private static class Scanner {
        private final InputStream input = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = input.read(buffer);
                position = 0;
                if (length < 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int token() throws IOException {
            int value = read();
            while (value <= ' ' && value != -1) {
                value = read();
            }
            return value;
        }

        int integer() throws IOException {
            int c = token();
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
            return value * sign;
        }
    }

    private static long sum(long[] tree, int end) {
        long result = 0;
        for (; end > 0; end -= end & -end) {
            result += tree[end];
        }
        return result;
    }

    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner();
        int n = scan.integer();
        int q = scan.integer();
        long[] x = new long[n];
        long[] y = new long[n];
        long[] prefix = new long[n + 1];
        long[] removed = new long[n + 1];
        for (int i = 0; i < n; ++i) {
            x[i] = scan.integer();
            y[i] = scan.integer();
        }
        for (int i = 0; i < n; ++i) {
            int j = (i + 1) % n;
            prefix[i + 1] = prefix[i] + x[i] * y[j] - y[i] * x[j];
        }
        long total = prefix[n];
        StringBuilder output = new StringBuilder();
        while (q-- > 0) {
            int type = scan.token();
            int left = scan.integer() - 1;
            int right = scan.integer() - 1;
            if (left > right) {
                int swap = left;
                left = right;
                right = swap;
            }
            long part = prefix[right] - prefix[left] + x[right] * y[left] - y[right] * x[left];
            part -= sum(removed, right) - sum(removed, left);
            long other = total - part;
            long answer = Math.max(part, other);
            if (type == 'c') {
                answer = Math.min(part, other);
                int edge = part < other ? left : right;
                // Charge the discarded area to the first edge of its original arc.
                for (int i = edge + 1; i <= n; i += i & -i) {
                    removed[i] += answer;
                }
                total -= answer;
            }
            output.append(answer / 2).append(answer % 2 == 0 ? ".0\n" : ".5\n");
        }
        System.out.print(output);
    }
}
