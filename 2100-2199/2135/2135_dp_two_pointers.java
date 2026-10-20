import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class Main {
    private static final int BUFFER_SIZE = 1 << 16;

    private static class FastInput {
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

        long nextLong() throws IOException {
            int current = read();
            while (current <= ' ' && current != -1) {
                current = read();
            }
            long value = 0;
            while (current > ' ') {
                value = value * 10 + current - '0';
                current = read();
            }
            return value;
        }
    }

    private static class ProductWindow {
        private final long bound;
        private long product = 1;
        private int left;

        ProductWindow(long bound) {
            this.bound = bound;
        }

        void advance(long[] values, int index) {
            long value = values[index];
            if (value > bound) {
                left = index + 1;
                product = 1;
                return;
            }
            // Divide before multiplying to keep the product within the bound.
            while (product > bound / value) {
                product /= values[left++];
            }
            product *= value;
        }
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int n = (int) input.nextLong();
        long lower = input.nextLong();
        long upper = input.nextLong();
        long[] values = new long[n];
        for (int i = 0; i < n; i++) {
            values[i] = input.nextLong();
        }

        int unreachable = n + 1;
        int[] dp = new int[n + 1];
        Arrays.fill(dp, unreachable);
        dp[0] = 0;
        int[] queue = new int[n + 1];
        int head = 0;
        int tail = 0;
        int nextCut = 0;
        ProductWindow large = new ProductWindow(upper);
        ProductWindow small = new ProductWindow(lower - 1);
        for (int i = 0; i < n; i++) {
            large.advance(values, i);
            small.advance(values, i);
            // Eligible cuts form a moving interval, so a minimum deque is enough.
            while (nextCut < small.left && nextCut <= i) {
                if (dp[nextCut] != unreachable) {
                    while (head < tail && dp[queue[tail - 1]] >= dp[nextCut]) {
                        tail--;
                    }
                    queue[tail++] = nextCut;
                }
                nextCut++;
            }
            while (head < tail && queue[head] < large.left) {
                head++;
            }
            if (head < tail) {
                dp[i + 1] = dp[queue[head]] + 1;
            }
        }
        System.out.println(dp[n] == unreachable ? -1 : dp[n]);
    }
}
