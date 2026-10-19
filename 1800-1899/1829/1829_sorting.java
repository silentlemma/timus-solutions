import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static final long FULL = (1L << Integer.SIZE) - 1;
    static final int BYTE = 8;

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens = new StringTokenizer("");

    static String next() throws IOException {
        while (!tokens.hasMoreTokens()) {
            tokens = new StringTokenizer(in.readLine());
        }
        return tokens.nextToken();
    }

    // a dotted address read byte by byte
    static long address(String text) {
        long value = 0;
        for (String part : text.split("\\.")) {
            value = value << BYTE | Integer.parseInt(part);
        }
        return value;
    }

    // each row covers one aligned block of addresses, and two blocks are
    // nested or apart; sweeping them by start, larger first, with a stack
    // of open blocks cuts the line into pieces routed by the innermost one
    static List<long[]> pieces(long[][] blocks) {
        Arrays.sort(blocks, (x, y) -> x[0] != y[0] ? Long.compare(x[0], y[0])
                                                   : Long.compare(y[1], x[1]));
        List<long[]> out = new ArrayList<>();
        List<long[]> stack = new ArrayList<>();
        long pos = 0;
        for (int i = 0; i <= blocks.length; i++) {
            long[] b = i < blocks.length ? blocks[i] : new long[] {FULL + 1, FULL + 1, -1};
            while (!stack.isEmpty() && stack.get(stack.size() - 1)[1] < b[0]) {
                long[] top = stack.remove(stack.size() - 1);
                emit(out, pos, top[1], top[2]);
                pos = top[1] + 1;
            }
            if (!stack.isEmpty()) {
                emit(out, pos, b[0] - 1, stack.get(stack.size() - 1)[2]);
            }
            pos = b[0];
            stack.add(b);
        }
        return out;
    }

    // adjacent pieces with one gateway merge, so equal routing gives
    // equal lists
    static void emit(List<long[]> out, long lo, long hi, long gate) {
        if (lo > hi) {
            return;
        }
        long[] last = out.isEmpty() ? null : out.get(out.size() - 1);
        if (last != null && last[1] + 1 == lo && last[2] == gate) {
            last[1] = hi;
        } else {
            out.add(new long[] {lo, hi, gate});
        }
    }

    public static void main(String[] args) throws IOException {
        List<List<long[]>> tables = new ArrayList<>();
        for (int t = 0; t < 2; t++) {
            int count = Integer.parseInt(next());
            long[][] blocks = new long[count][];
            for (int i = 0; i < count; i++) {
                long d = address(next()), m = address(next()), g = address(next());
                blocks[i] = new long[] {d & m, (d & m) | (FULL ^ m), g};
            }
            tables.add(pieces(blocks));
        }
        List<long[]> a = tables.get(0), b = tables.get(1);
        boolean same = a.size() == b.size();
        for (int i = 0; same && i < a.size(); i++) {
            same = Arrays.equals(a.get(i), b.get(i));
        }
        System.out.println(same ? "YES" : "NO");
    }
}
