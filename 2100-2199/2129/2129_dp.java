import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class Main {
    private static final long MODULUS = 1000000007L;
    private static final int BUFFER_SIZE = 8192;

    private static long countWays(long n, long base, long coins) {
        if (n < coins) {
            return 0;
        }
        long[] digits = new long[Long.SIZE];
        int levels = 0;
        long digitSum = 0;
        for (long value = n; value > 0; value /= base) {
            digits[levels] = value % base;
            digitSum += digits[levels++];
        }
        if (digitSum > coins || (coins - digitSum) % (base - 1) != 0) {
            return 0;
        }
        int budget = (int) ((coins - digitSum) / (base - 1));
        if (budget == 0) {
            return 1;
        }
        long[][] dp = makeRows(budget);
        long[][] next = makeRows(budget);
        dp[0][0] = 1;
        for (int level = levels - 1; level > 0; level--) {
            for (long[] row : next) {
                Arrays.fill(row, 0);
            }
            for (int used = 0; used <= budget; used++) {
                long[] row = dp[used];
                long suffix = 0;
                boolean hasValue = false;
                for (long ways : row) {
                    suffix += ways;
                    if (suffix >= MODULUS) {
                        suffix -= MODULUS;
                    }
                    hasValue |= ways != 0;
                }
                if (!hasValue) {
                    continue;
                }
                int threshold = 0;
                for (int splits = 0; splits <= budget - used; splits++) {
                    // Previous splits must supply enough coins at this level.
                    while (threshold < row.length
                            && digits[level] + base * threshold < splits) {
                        suffix -= row[threshold++];
                        if (suffix < 0) {
                            suffix += MODULUS;
                        }
                    }
                    if (threshold == row.length) {
                        break;
                    }
                    next[used + splits][splits] = suffix;
                }
            }
            long[][] previous = dp;
            dp = next;
            next = previous;
        }
        long answer = 0;
        for (long ways : dp[budget]) {
            answer += ways;
            if (answer >= MODULUS) {
                answer -= MODULUS;
            }
        }
        return answer;
    }

    private static long[][] makeRows(int budget) {
        long[][] rows = new long[budget + 1][];
        for (int used = 0; used <= budget; used++) {
            rows[used] = new long[used + 1];
        }
        return rows;
    }

    private static final class FastInput {
        private final InputStream input = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int size;

        private int read() throws IOException {
            if (position == size) {
                size = input.read(buffer);
                position = 0;
                if (size < 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        private long nextLong() throws IOException {
            int next = read();
            while (next <= ' ' && next != -1) {
                next = read();
            }
            long value = 0;
            while (next >= '0' && next <= '9') {
                value = value * 10 + next - '0';
                next = read();
            }
            return value;
        }
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        StringBuilder output = new StringBuilder();
        int cases = (int) input.nextLong();
        for (int index = 0; index < cases; index++) {
            long n = input.nextLong();
            long base = input.nextLong();
            long coins = input.nextLong();
            output.append(countWays(n, base, coins)).append('\n');
        }
        System.out.print(output);
    }
}
