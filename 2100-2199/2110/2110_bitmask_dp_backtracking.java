import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int SMALL_REMOVALS = 7;
    private static final int BUFFER_SIZE = 1 << 16;
    private static int[] values;
    private static int[] suffix;
    private static int best;

    private static final BufferedInputStream INPUT =
            new BufferedInputStream(System.in, BUFFER_SIZE);

    private static int nextInt() throws IOException {
        int ch = INPUT.read();
        while (ch <= ' ' && ch != -1) {
            ch = INPUT.read();
        }
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * 10 + ch - '0';
            ch = INPUT.read();
        }
        return value;
    }

    private static void visit(int index, int needed, int current) {
        if (needed == 0) {
            best = Math.max(best, current);
            return;
        }
        int upper = current | suffix[index];
        if (upper <= best) {
            return;
        }
        // One witness per uncovered bit suffices; extra places can be filled.
        if (needed == values.length - index
                || needed >= Integer.bitCount(suffix[index] & ~current)) {
            best = upper;
            return;
        }
        visit(index + 1, needed - 1, current | values[index]);
        visit(index + 1, needed, current);
    }

    private static int search(int kept) {
        suffix = new int[values.length + 1];
        for (int i = values.length - 1; i >= 0; --i) {
            suffix[i] = suffix[i + 1] | values[i];
        }
        best = 0;
        for (int i = 0; i < kept; ++i) {
            best |= values[i];
        }
        visit(0, kept, 0);
        return best;
    }

    private static int solveDp(int kept, int full) {
        int[] count = new int[full + 1];
        Arrays.fill(count, kept + 1);
        count[0] = 0;
        int upper = 0;
        int answer = 0;
        int previous = -1;
        for (int value : values) {
            if (value == previous) {
                continue;
            }
            previous = value;
            // Descending updates use each element at most once.
            for (int mask = upper; mask >= 0; --mask) {
                if (count[mask] < kept) {
                    int merged = mask | value;
                    count[merged] = Math.min(count[merged], count[mask] + 1);
                    answer = Math.max(answer, merged);
                }
            }
            upper |= value;
            if (answer == full) {
                break;
            }
        }
        return answer;
    }

    public static void main(String[] args) throws IOException {
        int n = nextInt();
        int removed = nextInt();
        values = new int[n];
        int full = 0;
        for (int i = 0; i < n; ++i) {
            values[i] = nextInt();
            full |= values[i];
        }
        int kept = n - removed;
        int answer = full;
        if (kept < Integer.bitCount(full)) {
            Arrays.sort(values);
            for (int i = 0; i < n / 2; ++i) {
                int other = n - 1 - i;
                int value = values[i];
                values[i] = values[other];
                values[other] = value;
            }
            answer = removed <= SMALL_REMOVALS ? search(kept) : solveDp(kept, full);
        }
        System.out.println(answer);
    }
}
