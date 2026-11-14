import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int DECIMAL = 10;
    private static final int PERCENT = 100;
    private static final long OUTPUT_SCALE = 100000000;
    // Denominators at most 9999 give gaps greater than 1 / SORT_SCALE.
    private static final long SORT_SCALE = 1L << 32;
    private static final int FRACTION_BITS = 14;
    private static final int FRACTION_MASK = (1 << FRACTION_BITS) - 1;
    private static final long NO_SHARE = 1;
    private static final long FULL_SHARE = encode(1, 1);

    private static int number(BufferedInputStream input) throws IOException {
        int ch = input.read();
        while (ch >= 0 && ch <= ' ') {
            ch = input.read();
        }
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = DECIMAL * value + ch - '0';
            ch = input.read();
        }
        return value;
    }

    private static long encode(int num, int den) {
        long key = SORT_SCALE * num / den;
        return ((key << FRACTION_BITS | num) << FRACTION_BITS) | den;
    }

    private static int numerator(long fraction) {
        return (int)(fraction >>> FRACTION_BITS) & FRACTION_MASK;
    }

    private static int denominator(long fraction) { return (int)fraction & FRACTION_MASK; }

    private static long maximumShare(int[] head, int[] sibling, int[] days, int deadline) {
        int n = head.length;
        int[] order = new int[n];
        int length = 1;
        int largestFamily = 0;
        for (int i = 0; i < length; i++) {
            int node = order[i];
            int family = 0;
            for (int child = head[node]; child != 0; child = sibling[child]) {
                days[child] += days[node];
                order[length++] = child;
                family++;
            }
            largestFamily = Math.max(largestFamily, family);
        }
        long[] limits = new long[n];
        long[] ranked = new long[largestFamily];
        for (int i = n - 1; i >= 0; i--) {
            int node = order[i];
            if (days[node] > deadline) {
                limits[node] = NO_SHARE;
                continue;
            }
            int count = 0;
            for (int child = head[node]; child != 0; child = sibling[child]) {
                ranked[count++] = limits[child];
            }
            Arrays.sort(ranked, 0, count);
            limits[node] = FULL_SHARE;
            for (int rank = 1; rank <= count; rank++) {
                long limit = ranked[count - rank];
                int num = numerator(limit), den = denominator(limit);
                // The rank bounds the share by both rank/count and the child's limit.
                if (rank * den >= num * count) {
                    limits[node] = (rank - 1) * den < num * count ? limit : encode(rank - 1, count);
                    break;
                }
            }
        }
        return limits[0];
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int n = number(input), deadline = number(input);
        int[] head = new int[n], sibling = new int[n], days = new int[n];
        for (int node = 1; node < n; node++) {
            int parent = number(input) - 1;
            days[node] = number(input);
            sibling[node] = head[parent];
            head[parent] = node;
        }
        long share = maximumShare(head, sibling, days, deadline);
        int den = denominator(share);
        long value = (PERCENT * OUTPUT_SCALE * numerator(share) + den / 2) / den;
        String decimals = Long.toString(OUTPUT_SCALE + value % OUTPUT_SCALE).substring(1);
        System.out.println(value / OUTPUT_SCALE + "." + decimals);
    }
}
