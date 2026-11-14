import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int DECIMAL = 10;
    private static final int LIMB_LIMIT = 1000000;
    private static final int BINARY_BITS = 60;
    private static final long BINARY_BASE = 1L << BINARY_BITS;

    private static int number(BufferedInputStream input) throws IOException {
        int digit = input.read();
        while (digit >= 0 && digit <= ' ') {
            digit = input.read();
        }
        int value = 0;
        while (digit >= '0' && digit <= '9') {
            value = value * DECIMAL + digit - '0';
            digit = input.read();
        }
        return value;
    }

    private static int binarySum(long value, long mask, int bits) {
        int sum = Long.bitCount(value & mask);
        for (int bit = 1; bit < bits; ++bit) {
            sum += Long.bitCount((value >>> bit) & mask) << bit;
        }
        return sum;
    }

    private static int[] costs(int radix, int count) {
        int bits = (radix & (radix - 1)) == 0 ? Integer.numberOfTrailingZeros(radix) : 0;
        int tableBase = 1;
        long mask = 0;
        byte[] sums;
        if (bits == 0) {
            while (tableBase <= LIMB_LIMIT / radix) {
                tableBase *= radix;
            }
            sums = new byte[tableBase];
            for (int i = 1; i < tableBase; ++i) {
                sums[i] = (byte)(sums[i / radix] + i % radix);
            }
        } else {
            sums = null;
            for (int bit = 0; bit < BINARY_BITS; bit += bits) {
                mask |= 1L << bit;
            }
        }

        long base = bits == 0 ? tableBase : BINARY_BASE;
        int limbBits = Long.SIZE - 1 - Long.numberOfLeadingZeros(base);
        // F(count) is below 2^count, and each limb holds at least limbBits binary digits.
        int capacity = (count + limbBits - 1) / limbBits;
        long[] previous = new long[capacity];
        long[] current = new long[capacity];
        previous[0] = current[0] = 1;
        int length = 1;
        int[] cost = new int[count];
        cost[0] = cost[1] = 1;
        for (int i = 2; i < count; ++i) {
            int carry = 0;
            int sum = 0;
            for (int j = 0; j < length; ++j) {
                long value = previous[j] + current[j] + carry;
                carry = value >= base ? 1 : 0;
                value -= carry * base;
                previous[j] = value;
                sum += bits == 0 ? sums[(int)value] : binarySum(value, mask, bits);
            }
            if (carry != 0) {
                previous[length++] = carry;
            }
            cost[i] = sum + carry;
            long[] swap = previous;
            previous = current;
            current = swap;
        }
        return cost;
    }

    private static int[] stableOrder(int[] costs) {
        int maximum = 0;
        for (int cost : costs) {
            maximum = Math.max(maximum, cost);
        }
        int[] start = new int[maximum + 1];
        for (int cost : costs) {
            ++start[cost];
        }
        int offset = 0;
        for (int i = 0; i < start.length; ++i) {
            int frequency = start[i];
            start[i] = offset;
            offset += frequency;
        }
        int[] order = new int[costs.length];
        for (int i = 0; i < costs.length; ++i) {
            order[start[costs[i]]++] = i + 1;
        }
        return order;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int radix = number(input);
        int count = number(input);
        int[] order = stableOrder(costs(radix, count));
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < count; ++i) {
            if (i != 0) {
                output.append(' ');
            }
            output.append(order[i]);
        }
        System.out.println(output);
    }
}
