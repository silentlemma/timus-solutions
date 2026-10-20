import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int BUFFER_SIZE = 1 << 16;
    private static final int SPACE = ' ';
    private static final int ZERO = '0';
    private static final int NINE = '9';

    private static final class Input {
        private final BufferedInputStream source = new BufferedInputStream(System.in, BUFFER_SIZE);

        int nextInt() throws IOException {
            int ch;
            do {
                ch = source.read();
            } while (ch <= SPACE && ch != -1);
            int value = 0;
            while (ch >= ZERO && ch <= NINE) {
                value = value * 10 + ch - ZERO;
                ch = source.read();
            }
            return value;
        }
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        int n = input.nextInt();
        int days = input.nextInt();
        int length = input.nextInt();
        int moves = input.nextInt();
        int positions = n - length + 1;
        long[][] dp = new long[1][positions];
        long[] prefix = new long[n + 1];
        long[] weight = new long[positions];
        long[] key = new long[positions];
        int[] queue = new int[positions];
        int previousLow = 0;

        for (int day = 1; day <= days; day++) {
            for (int j = 0; j < n; j++) {
                prefix[j + 1] = prefix[j] + input.nextInt();
            }
            for (int x = 0; x < positions; x++) {
                weight[x] = prefix[x + length] - prefix[x];
            }
            int low = Math.max(0, moves - (days - day));
            int high = Math.min(day, moves);
            long[][] next = new long[high - low + 1][positions];
            for (int used = low; used <= high; used++) {
                long[] current = next[used - low];
                if (used < day) {
                    long[] stay = dp[used - previousLow];
                    for (int x = 0; x < positions; x++) {
                        current[x] = stay[x] + weight[x];
                    }
                }
                if (used == 0) {
                    continue;
                }
                long[] previous = dp[used - 1 - previousLow];
                for (int x = 0; x < positions; x++) {
                    key[x] = previous[x] - prefix[x];
                }
                int head = 0;
                int tail = 0;
                long best = 0;
                for (int y = 0; y < positions; y++) {
                    if (y >= length) {
                        int x = y - length;
                        best = Math.max(best, previous[x] + weight[x]);
                    }
                    while (head < tail && key[queue[tail - 1]] <= key[y]) {
                        tail--;
                    }
                    queue[tail++] = y;
                    if (queue[head] <= y - length) {
                        head++;
                    }
                    long overlap = key[queue[head]] + prefix[y + length];
                    current[y] = Math.max(current[y], Math.max(overlap, best + weight[y]));
                }
                for (int x = 0; x < positions; x++) {
                    key[x] = previous[x] + prefix[x + length];
                }
                head = 0;
                tail = 0;
                best = 0;
                for (int y = positions - 1; y >= 0; y--) {
                    if (y + length < positions) {
                        int x = y + length;
                        best = Math.max(best, previous[x] + weight[x]);
                    }
                    while (head < tail && key[queue[tail - 1]] <= key[y]) {
                        tail--;
                    }
                    queue[tail++] = y;
                    if (queue[head] >= y + length) {
                        head++;
                    }
                    long overlap = key[queue[head]] - prefix[y];
                    current[y] = Math.max(current[y], Math.max(overlap, best + weight[y]));
                }
            }
            dp = next;
            previousLow = low;
        }
        long answer = 0;
        for (long value : dp[0]) {
            answer = Math.max(answer, value);
        }
        System.out.println(answer);
    }
}
