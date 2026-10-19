import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int PERCENT = 100;
    private static final int MAX_PRICE = 50000;
    private static final int BUFFER_SIZE = 65536;

    private static final class FastInput {
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = System.in.read(buffer);
                position = 0;
                if (length < 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int nextInt() throws IOException {
            int current = read();
            while (current >= 0 && current <= ' ') {
                current = read();
            }
            int value = 0;
            while (current >= '0' && current <= '9') {
                value = value * 10 + current - '0';
                current = read();
            }
            return value;
        }
    }

    private static final class PriceGroup {
        private int[] values = new int[1];
        private long[] prefix;
        private int size;

        void add(int value) {
            if (size == values.length) {
                values = Arrays.copyOf(values, size * 2);
            }
            values[size++] = value;
        }

        void prepare() {
            Arrays.sort(values, 0, size);
            prefix = new long[size + 1];
            for (int i = 0; i < size; i++) {
                prefix[i + 1] = prefix[i] + values[i];
            }
        }

        int upperBound(int limit) {
            int left = 0;
            int right = size;
            while (left < right) {
                int middle = (left + right) / 2;
                if (values[middle] <= limit) {
                    left = middle + 1;
                } else {
                    right = middle;
                }
            }
            return left;
        }
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int n = input.nextInt();
        int m = input.nextInt();
        PriceGroup[] groups = new PriceGroup[PERCENT + 1];
        for (int d = 0; d <= PERCENT; d++) {
            groups[d] = new PriceGroup();
        }
        long singles = 0;
        for (int i = 0; i < n; i++) {
            int price = input.nextInt();
            int discount = input.nextInt();
            groups[discount].add(price);
            singles += (long) price * (PERCENT - discount);
        }
        int[] minimum = new int[PERCENT + 1];
        Arrays.fill(minimum, n + 1);
        for (int i = 0; i < m; i++) {
            int needed = input.nextInt();
            int discount = input.nextInt();
            minimum[discount] = Math.min(minimum[discount], needed);
        }
        int[] count = new int[PERCENT + 1];
        long[] priceSum = new long[PERCENT + 1];
        long[] weightedSum = new long[PERCENT + 1];
        for (int d = 0; d <= PERCENT; d++) {
            groups[d].prepare();
            long groupSum = groups[d].prefix[groups[d].size];
            count[d] = groups[d].size;
            priceSum[d] = groupSum;
            weightedSum[d] = groupSum * d;
            if (d > 0) {
                count[d] += count[d - 1];
                priceSum[d] += priceSum[d - 1];
                weightedSum[d] += weightedSum[d - 1];
            }
        }
        long best = singles;
        int smallestRequirement = n + 1;
        for (int p = PERCENT; p > 0; p--) {
            if (minimum[p] >= smallestRequirement) {
                continue;
            }
            smallestRequirement = minimum[p];
            long candidate = singles + weightedSum[p] - p * priceSum[p];
            if (candidate >= best) {
                continue;
            }
            int needed = minimum[p] - count[p];
            if (needed > 0) {
                // Find the last penalty among the required cheapest extra tickets.
                int left = 0;
                int right = MAX_PRICE * (PERCENT - p);
                while (left < right) {
                    int middle = (left + right) / 2;
                    int taken = 0;
                    for (int d = p + 1; d <= PERCENT; d++) {
                        taken += groups[d].upperBound(middle / (d - p));
                    }
                    if (taken >= needed) {
                        right = middle;
                    } else {
                        left = middle + 1;
                    }
                }
                int taken = 0;
                for (int d = p + 1; d <= PERCENT; d++) {
                    int amount = groups[d].upperBound(left / (d - p));
                    taken += amount;
                    candidate += groups[d].prefix[amount] * (d - p);
                }
                candidate -= (long) (taken - needed) * left;
            }
            best = Math.min(best, candidate);
        }
        long fraction = best % PERCENT;
        System.out.println(best / PERCENT + "." + (fraction < 10 ? "0" : "") + fraction);
    }
}
