import java.io.IOException;
import java.io.InputStream;

public class Main {
    private static final int ABSENT = -1;
    private static final int INPUT_BUFFER_SIZE = 65536;

    private static class FastInput {
        private final InputStream input = System.in;
        private final byte[] buffer = new byte[INPUT_BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = input.read(buffer);
                position = 0;
                if (length < 0) {
                    return ABSENT;
                }
            }
            return buffer[position++];
        }

        long nextLong() throws IOException {
            int ch = read();
            while (ch <= ' ') {
                ch = read();
            }
            long value = 0;
            while (ch >= '0' && ch <= '9') {
                value = value * 10 + ch - '0';
                ch = read();
            }
            return value;
        }
    }

    private static boolean better(int left, int right, long[] values) {
        return values[left] > values[right]
                || (values[left] == values[right] && left < right);
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int n = (int) input.nextLong();
        long[] values = new long[n];
        int[] following = new int[n];
        for (int i = 0; i < n; ++i) {
            values[i] = input.nextLong();
            following[i] = ABSENT;
        }
        int last = 0;
        int count = 1;
        for (int i = 1; i < n; ++i) {
            if (values[i] > values[last]) {
                following[last] = i;
                last = i;
                ++count;
            }
        }
        following[last] = n;

        // The earliest maximum of a prefix is its final staircase element.
        int[] tree = new int[n + 1];
        for (int i = 1; i <= n; ++i) {
            tree[i] = i - 1;
        }
        for (int i = 1; i <= n; ++i) {
            int parent = i + (i & -i);
            if (parent <= n && better(tree[i], tree[parent], values)) {
                tree[parent] = tree[i];
            }
        }

        StringBuilder output = new StringBuilder();
        int queries = (int) input.nextLong();
        for (int query = 0; query < queries; ++query) {
            int position = (int) input.nextLong() - 1;
            long increase = input.nextLong();
            if (increase == 0) {
                output.append(count).append('\n');
                continue;
            }
            values[position] += increase;
            if (following[position] == ABSENT) {
                int previous = 0;
                for (int i = position; i > 0; i -= i & -i) {
                    if (better(tree[i], previous, values)) {
                        previous = tree[i];
                    }
                }
                if (values[position] > values[previous]) {
                    following[position] = following[previous];
                    following[previous] = position;
                    ++count;
                }
            }
            if (following[position] != ABSENT) {
                int successor = following[position];
                while (successor < n && values[successor] <= values[position]) {
                    int removed = successor;
                    successor = following[removed];
                    following[removed] = ABSENT;
                    --count;
                }
                following[position] = successor;
            }

            for (int i = position + 1; i <= n; i += i & -i) {
                if (tree[i] != position) {
                    if (!better(position, tree[i], values)) {
                        break;
                    }
                    tree[i] = position;
                }
            }
            output.append(count).append('\n');
        }
        System.out.print(output);
    }
}
