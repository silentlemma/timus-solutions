import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Main {
    private static final int TERNARY_BASE = 3;
    private static final int WORD_BITS = Long.SIZE;
    private static final int MAX_DP_SUM = 50_000_000;
    private static final int INPUT_BUFFER_SIZE = 65536;
    private static final BufferedInputStream INPUT =
            new BufferedInputStream(System.in, INPUT_BUFFER_SIZE);

    private static int nextInt() throws IOException {
        int c = INPUT.read();
        while (c <= ' ' && c != -1) {
            c = INPUT.read();
        }
        int value = 0;
        while (c > ' ') {
            value = value * 10 + c - '0';
            c = INPUT.read();
        }
        return value;
    }

    private static void collect(int value, int pattern, int mask, int limit,
                                ArrayList<Integer> coins) {
        for (int shifted = value; shifted >= pattern; shifted >>>= 1) {
            if ((shifted & mask) == pattern) {
                coins.add(value);
                break;
            }
        }
        long next = (long) value * TERNARY_BASE;
        if (next <= limit) {
            collect((int) next, pattern << 1, (mask << 1) | 1, limit, coins);
        }
        if (next + 1 <= limit) {
            collect((int) next + 1, (pattern << 1) | 1, (mask << 1) | 1, limit, coins);
        }
    }

    private static long[] subsetBits(ArrayList<Integer> coins, int count, int total) {
        long[] bits = new long[total / WORD_BITS + 1];
        bits[0] = 1;
        int reachable = 0;
        for (int i = 0; i < count; ++i) {
            int value = coins.get(i);
            int words = value / WORD_BITS;
            int offset = value % WORD_BITS;
            // Descending sources keep each coin available only once.
            for (int source = reachable / WORD_BITS; source >= 0; --source) {
                long word = bits[source];
                int target = source + words;
                bits[target] |= word << offset;
                if (offset != 0 && target + 1 < bits.length) {
                    bits[target + 1] |= word >>> (WORD_BITS - offset);
                }
            }
            reachable += value;
        }
        return bits;
    }

    public static void main(String[] args) throws IOException {
        int count = nextInt();
        int[] queries = new int[count];
        int limit = 0;
        for (int i = 0; i < count; ++i) {
            queries[i] = nextInt();
            limit = Math.max(limit, queries[i]);
        }
        ArrayList<Integer> coins = new ArrayList<>();
        collect(1, 1, 1, limit, coins);
        Collections.sort(coins);

        int smallCount = 0;
        int smallTotal = 0;
        while (smallCount < coins.size()
                && (long) smallTotal + coins.get(smallCount) <= MAX_DP_SUM) {
            smallTotal += coins.get(smallCount++);
        }
        long[] bits = subsetBits(coins, smallCount, smallTotal);
        long[] highSums = new long[1 << (coins.size() - smallCount)];
        int highCount = 1;
        for (int i = smallCount; i < coins.size(); ++i) {
            for (int j = 0; j < highCount; ++j) {
                highSums[highCount + j] = highSums[j] + coins.get(i);
            }
            highCount *= 2;
        }
        Arrays.sort(highSums);

        StringBuilder output = new StringBuilder();
        for (int query : queries) {
            boolean found = false;
            for (long high : highSums) {
                if (high > query) {
                    break;
                }
                long low = query - high;
                if (low <= smallTotal
                        && ((bits[(int) low / WORD_BITS] >>> (low % WORD_BITS)) & 1) != 0) {
                    found = true;
                    break;
                }
            }
            output.append(found ? "YES\n" : "NO\n");
        }
        System.out.print(output);
    }
}
