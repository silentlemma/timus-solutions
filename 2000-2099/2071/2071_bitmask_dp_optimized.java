import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int JUICES = 3;
    private static final int KINDS = (1 << JUICES) - 1;
    private static final int PINEAPPLE = 1 << (JUICES - 1);
    private static final byte UNREACHED = JUICES * KINDS + 1;
    private static final int DECIMAL_DIGITS = 10;

    private static int tokenStart(BufferedInputStream input) throws IOException {
        int c = input.read();
        while (c >= 0 && c <= ' ') {
            c = input.read();
        }
        return c;
    }

    private static int bestOrder(int present, int[] order) {
        // Costs and predecessors each fit in one byte.
        byte[] costs = new byte[(present + 1) * KINDS];
        byte[] previous = new byte[costs.length];
        Arrays.fill(costs, UNREACHED);
        for (int remaining = present; remaining != 0; remaining &= remaining - 1) {
            int kind = Integer.numberOfTrailingZeros(remaining);
            costs[(1 << kind) * KINDS + kind] = (byte)Integer.bitCount(kind + 1);
        }
        for (int used = 1; used < present; used++) {
            int available = present & ~used;
            for (int last = 0; last < KINDS; last++) {
                byte cost = costs[used * KINDS + last];
                if (cost == UNREACHED) {
                    continue;
                }
                for (int remaining = available; remaining != 0; remaining &= remaining - 1) {
                    int next = Integer.numberOfTrailingZeros(remaining);
                    int index = (used | (1 << next)) * KINDS + next;
                    int total = cost + Integer.bitCount((next + 1) & ~(last + 1));
                    if (total < costs[index]) {
                        costs[index] = (byte)total;
                        previous[index] = (byte)last;
                    }
                }
            }
        }
        int last = 0;
        for (int kind = 1; kind < KINDS; kind++) {
            if (costs[present * KINDS + kind] < costs[present * KINDS + last]) {
                last = kind;
            }
        }
        int result = costs[present * KINDS + last];
        for (int used = present, i = Integer.bitCount(present) - 1; used != 0; i--) {
            order[i] = last;
            int predecessor = previous[used * KINDS + last];
            used ^= 1 << last;
            last = predecessor;
        }
        return result;
    }

    private static void writeInt(BufferedOutputStream output, byte[] digits, int value)
        throws IOException {
        int start = digits.length;
        do {
            digits[--start] = (byte)('0' + value % 10);
            value /= 10;
        } while (value > 0);
        output.write(digits, start, digits.length - start);
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int count = 0;
        for (int c = tokenStart(input); c > ' '; c = input.read()) {
            count = count * 10 + c - '0';
        }
        int[] first = new int[KINDS];
        int[] next = new int[count + 1];
        int present = 0;
        for (int glass = 1; glass <= count; glass++) {
            int mask = 0;
            for (int c = tokenStart(input); c > ' '; c = input.read()) {
                mask |= c == 'A' ? 1 : (c == 'B' ? 2 : PINEAPPLE);
            }
            int kind = mask - 1;
            present |= 1 << kind;
            // Link the glasses of each type through one index array.
            next[glass] = first[kind];
            first[kind] = glass;
        }

        int[] order = new int[Integer.bitCount(present)];
        int minimum = bestOrder(present, order);
        BufferedOutputStream output = new BufferedOutputStream(System.out);
        byte[] digits = new byte[DECIMAL_DIGITS];
        writeInt(output, digits, minimum);
        int separator = '\n';
        for (int kind : order) {
            for (int glass = first[kind]; glass != 0; glass = next[glass]) {
                output.write(separator);
                writeInt(output, digits, glass);
                separator = ' ';
            }
        }
        output.write('\n');
        output.flush();
    }
}
